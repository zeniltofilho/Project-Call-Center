# Sistema de Call Center Desktop Completo com Dashboard Moderno
# Autor: ChatGPT
# Python + Tkinter + SQLite

import tkinter as tk
from tkinter import ttk, messagebox
import sqlite3
from datetime import datetime

DB = "callcenter.db"

# ---------------------- BANCO ----------------------


def conectar():
    return sqlite3.connect(DB)


def criar_tabelas():
    con = conectar()
    cur = con.cursor()

    cur.execute("""
    CREATE TABLE IF NOT EXISTS usuarios(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        usuario TEXT UNIQUE,
        senha TEXT
    )
    """)

    cur.execute("""
    CREATE TABLE IF NOT EXISTS clientes(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT,
        telefone TEXT,
        email TEXT
    )
    """)

    cur.execute("""
    CREATE TABLE IF NOT EXISTS operadores(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT
    )
    """)

    cur.execute("""
    CREATE TABLE IF NOT EXISTS atendimentos(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        cliente TEXT,
        operador TEXT,
        assunto TEXT,
        data TEXT
    )
    """)

    cur.execute(
        "INSERT OR IGNORE INTO usuarios(usuario, senha) VALUES('admin','123')")

    con.commit()
    con.close()

# ---------------------- LOGIN ----------------------


class LoginWindow:
    def __init__(self, master):
        self.master = master
        master.title("Login - Call Center")
        master.geometry("350x250")
        master.configure(bg="#1f2933")

        style = ttk.Style()
        style.theme_use('clam')

        tk.Label(master, text="Sistema Call Center", fg="white",
                 bg="#1f2933", font=("Segoe UI", 16, "bold")).pack(pady=15)

        tk.Label(master, text="Usuário", fg="white", bg="#1f2933").pack()
        self.usuario = ttk.Entry(master)
        self.usuario.pack(pady=5)

        tk.Label(master, text="Senha", fg="white", bg="#1f2933").pack()
        self.senha = ttk.Entry(master, show="*")
        self.senha.pack(pady=5)

        ttk.Button(master, text="Entrar", command=self.login).pack(pady=15)

    def login(self):
        con = conectar()
        cur = con.cursor()
        cur.execute("SELECT * FROM usuarios WHERE usuario=? AND senha=?",
                    (self.usuario.get(), self.senha.get()))
        res = cur.fetchone()
        con.close()

        if res:
            self.master.destroy()
            abrir_sistema()
        else:
            messagebox.showerror("Erro", "Login inválido")

# ---------------------- SISTEMA PRINCIPAL ----------------------


class Sistema:
    def __init__(self, master):
        self.master = master
        master.title("Sistema Call Center - Dashboard")
        master.geometry("1100x650")
        master.configure(bg="#f3f4f6")

        style = ttk.Style()
        style.theme_use('clam')

        style.configure("TNotebook.Tab", font=(
            "Segoe UI", 11, "bold"), padding=[12, 8])
        style.configure("Card.TFrame", background="white", relief="raised")
        style.configure("CardTitle.TLabel", font=(
            "Segoe UI", 12, "bold"), background="white")
        style.configure("CardValue.TLabel", font=(
            "Segoe UI", 22, "bold"), foreground="#2563eb", background="white")

        self.notebook = ttk.Notebook(master)
        self.notebook.pack(fill="both", expand=True, padx=10, pady=10)

        self.tela_dashboard()
        self.tela_clientes()
        self.tela_operadores()
        self.tela_atendimentos()
        self.tela_relatorios()

    # ---------------- DASHBOARD ----------------
    def tela_dashboard(self):
        frame = ttk.Frame(self.notebook)
        self.notebook.add(frame, text="Dashboard")

        topo = ttk.Label(frame, text="Visão Geral do Sistema",
                         font=("Segoe UI", 18, "bold"))
        topo.pack(pady=15)

        cards_frame = ttk.Frame(frame)
        cards_frame.pack(pady=20)

        self.card_clientes = self.criar_card(
            cards_frame, "Clientes Cadastrados")
        self.card_operadores = self.criar_card(cards_frame, "Operadores")
        self.card_atendimentos = self.criar_card(cards_frame, "Atendimentos")

        self.card_clientes.grid(row=0, column=0, padx=15)
        self.card_operadores.grid(row=0, column=1, padx=15)
        self.card_atendimentos.grid(row=0, column=2, padx=15)

        ttk.Button(frame, text="Atualizar Dashboard",
                   command=self.atualizar_dashboard).pack(pady=15)

        self.atualizar_dashboard()

    def criar_card(self, parent, titulo):
        card = ttk.Frame(parent, style="Card.TFrame", width=200, height=120)

        lbl_titulo = ttk.Label(card, text=titulo, style="CardTitle.TLabel")
        lbl_titulo.pack(pady=(15, 5))

        lbl_valor = ttk.Label(card, text="0", style="CardValue.TLabel")
        lbl_valor.pack()

        card.lbl_valor = lbl_valor

        return card

    def atualizar_dashboard(self):
        con = conectar()
        cur = con.cursor()

        cur.execute("SELECT COUNT(*) FROM clientes")
        self.card_clientes.lbl_valor.config(text=str(cur.fetchone()[0]))

        cur.execute("SELECT COUNT(*) FROM operadores")
        self.card_operadores.lbl_valor.config(text=str(cur.fetchone()[0]))

        cur.execute("SELECT COUNT(*) FROM atendimentos")
        self.card_atendimentos.lbl_valor.config(text=str(cur.fetchone()[0]))

        con.close()

    # ---------------- CLIENTES ----------------
    def tela_clientes(self):
        frame = ttk.Frame(self.notebook)
        self.notebook.add(frame, text="Clientes")

        form = ttk.LabelFrame(frame, text="Cadastro de Cliente")
        form.pack(fill="x", padx=10, pady=10)

        ttk.Label(form, text="Nome").grid(row=0, column=0, padx=5, pady=5)
        ttk.Label(form, text="Telefone").grid(row=0, column=2, padx=5, pady=5)
        ttk.Label(form, text="Email").grid(row=0, column=4, padx=5, pady=5)

        self.cli_nome = ttk.Entry(form)
        self.cli_tel = ttk.Entry(form)
        self.cli_email = ttk.Entry(form)

        self.cli_nome.grid(row=0, column=1, padx=5)
        self.cli_tel.grid(row=0, column=3, padx=5)
        self.cli_email.grid(row=0, column=5, padx=5)

        ttk.Button(form, text="Salvar", command=self.salvar_cliente).grid(
            row=0, column=6, padx=10)
        ttk.Button(form, text="Excluir", command=self.excluir_cliente).grid(
            row=0, column=7)

        self.lista_clientes = ttk.Treeview(frame, columns=(
            "id", "nome", "tel", "email"), show="headings")
        for c in ("id", "nome", "tel", "email"):
            self.lista_clientes.heading(c, text=c)
        self.lista_clientes.pack(fill="both", expand=True, padx=10, pady=10)

        self.lista_clientes.bind("<ButtonRelease-1>", self.selecionar_cliente)

        self.carregar_clientes()

    def salvar_cliente(self):
        con = conectar()
        cur = con.cursor()
        cur.execute("INSERT INTO clientes(nome,telefone,email) VALUES(?,?,?)",
                    (self.cli_nome.get(), self.cli_tel.get(), self.cli_email.get()))
        con.commit()
        con.close()
        self.carregar_clientes()
        self.atualizar_dashboard()

    def carregar_clientes(self):
        for i in self.lista_clientes.get_children():
            self.lista_clientes.delete(i)

        con = conectar()
        cur = con.cursor()
        for row in cur.execute("SELECT * FROM clientes"):
            self.lista_clientes.insert("", "end", values=row)
        con.close()

    def selecionar_cliente(self, e):
        item = self.lista_clientes.item(self.lista_clientes.focus())
        if item['values']:
            self.cli_nome.delete(0, tk.END)
            self.cli_tel.delete(0, tk.END)
            self.cli_email.delete(0, tk.END)

            self.cli_nome.insert(0, item['values'][1])
            self.cli_tel.insert(0, item['values'][2])
            self.cli_email.insert(0, item['values'][3])

    def excluir_cliente(self):
        item = self.lista_clientes.item(self.lista_clientes.focus())
        if not item['values']:
            return
        con = conectar()
        cur = con.cursor()
        cur.execute("DELETE FROM clientes WHERE id=?", (item['values'][0],))
        con.commit()
        con.close()
        self.carregar_clientes()
        self.atualizar_dashboard()

    # ---------------- OPERADORES ----------------
    def tela_operadores(self):
        frame = ttk.Frame(self.notebook)
        self.notebook.add(frame, text="Operadores")

        form = ttk.LabelFrame(frame, text="Cadastro de Operador")
        form.pack(fill="x", padx=10, pady=10)

        ttk.Label(form, text="Nome do Operador").grid(
            row=0, column=0, padx=5, pady=5)
        self.op_nome = ttk.Entry(form)
        self.op_nome.grid(row=0, column=1, padx=5)

        ttk.Button(form, text="Salvar", command=self.salvar_operador).grid(
            row=0, column=2, padx=10)
        ttk.Button(form, text="Excluir", command=self.excluir_operador).grid(
            row=0, column=3)

        self.lista_operadores = ttk.Treeview(
            frame, columns=("id", "nome"), show="headings")
        self.lista_operadores.heading("id", text="ID")
        self.lista_operadores.heading("nome", text="Nome")
        self.lista_operadores.pack(fill="both", expand=True, padx=10, pady=10)

        self.carregar_operadores()

    def salvar_operador(self):
        con = conectar()
        cur = con.cursor()
        cur.execute("INSERT INTO operadores(nome) VALUES(?)",
                    (self.op_nome.get(),))
        con.commit()
        con.close()
        self.carregar_operadores()
        self.atualizar_dashboard()

    def carregar_operadores(self):
        for i in self.lista_operadores.get_children():
            self.lista_operadores.delete(i)

        con = conectar()
        cur = con.cursor()
        for row in cur.execute("SELECT * FROM operadores"):
            self.lista_operadores.insert("", "end", values=row)
        con.close()

    def excluir_operador(self):
        item = self.lista_operadores.item(self.lista_operadores.focus())
        if not item['values']:
            return
        con = conectar()
        cur = con.cursor()
        cur.execute("DELETE FROM operadores WHERE id=?", (item['values'][0],))
        con.commit()
        con.close()
        self.carregar_operadores()
        self.atualizar_dashboard()

    # ---------------- ATENDIMENTOS ----------------
    def tela_atendimentos(self):
        frame = ttk.Frame(self.notebook)
        self.notebook.add(frame, text="Atendimentos")

        form = ttk.LabelFrame(frame, text="Registrar Atendimento")
        form.pack(fill="x", padx=10, pady=10)

        ttk.Label(form, text="Cliente").grid(row=0, column=0, padx=5, pady=5)
        ttk.Label(form, text="Operador").grid(row=0, column=2, padx=5, pady=5)
        ttk.Label(form, text="Assunto").grid(row=0, column=4, padx=5, pady=5)

        self.at_cliente = ttk.Entry(form)
        self.at_operador = ttk.Entry(form)
        self.at_assunto = ttk.Entry(form)

        self.at_cliente.grid(row=0, column=1, padx=5)
        self.at_operador.grid(row=0, column=3, padx=5)
        self.at_assunto.grid(row=0, column=5, padx=5)

        ttk.Button(form, text="Registrar", command=self.salvar_atendimento).grid(
            row=0, column=6, padx=10)

        self.lista_atendimentos = ttk.Treeview(frame, columns=(
            "id", "cliente", "operador", "assunto", "data"), show="headings")
        for c in ("id", "cliente", "operador", "assunto", "data"):
            self.lista_atendimentos.heading(c, text=c)
        self.lista_atendimentos.pack(
            fill="both", expand=True, padx=10, pady=10)

        self.carregar_atendimentos()

    def salvar_atendimento(self):
        data = datetime.now().strftime("%d/%m/%Y %H:%M")
        con = conectar()
        cur = con.cursor()
        cur.execute("INSERT INTO atendimentos(cliente,operador,assunto,data) VALUES(?,?,?,?)",
                    (self.at_cliente.get(), self.at_operador.get(), self.at_assunto.get(), data))
        con.commit()
        con.close()
        self.carregar_atendimentos()
        self.atualizar_dashboard()

    def carregar_atendimentos(self):
        for i in self.lista_atendimentos.get_children():
            self.lista_atendimentos.delete(i)

        con = conectar()
        cur = con.cursor()
        for row in cur.execute("SELECT * FROM atendimentos ORDER BY id DESC"):
            self.lista_atendimentos.insert("", "end", values=row)
        con.close()

    # ---------------- RELATÓRIOS ----------------
    def tela_relatorios(self):
        frame = ttk.Frame(self.notebook)
        self.notebook.add(frame, text="Relatórios")

        ttk.Label(frame, text="Relatórios Gerais", font=(
            "Segoe UI", 16, "bold")).pack(pady=20)

        self.lbl_clientes = ttk.Label(
            frame, text="Clientes: 0", font=("Segoe UI", 12))
        self.lbl_clientes.pack(pady=5)

        self.lbl_atend = ttk.Label(
            frame, text="Atendimentos: 0", font=("Segoe UI", 12))
        self.lbl_atend.pack(pady=5)

        ttk.Button(frame, text="Atualizar",
                   command=self.atualizar_relatorios).pack(pady=15)

        self.atualizar_relatorios()

    def atualizar_relatorios(self):
        con = conectar()
        cur = con.cursor()

        cur.execute("SELECT COUNT(*) FROM clientes")
        clientes = cur.fetchone()[0]

        cur.execute("SELECT COUNT(*) FROM atendimentos")
        atend = cur.fetchone()[0]

        self.lbl_clientes.config(text=f"Clientes: {clientes}")
        self.lbl_atend.config(text=f"Atendimentos: {atend}")

        con.close()

# ---------------------- INICIALIZAÇÃO ----------------------


def abrir_sistema():
    root = tk.Tk()
    Sistema(root)
    root.mainloop()


if __name__ == '__main__':
    criar_tabelas()

    root = tk.Tk()
    LoginWindow(root)
    root.mainloop()
