import tkinter as tk
from tkinter import ttk, messagebox


class SistemaContribuintes:

    def __init__(self, root):
        self.root = root
        self.root.title("Contribuintes")
        self.root.geometry("1300x700")

        self.criar_topo()
        self.criar_tabela()
        self.criar_painel_inferior()

    # ================= TOPO =================
    def criar_topo(self):
        frame_top = tk.Frame(self.root, bg="#dcdcdc", height=60)
        frame_top.pack(fill="x")

        tk.Button(frame_top, text="Cadastrar Doações",
                  width=18).pack(side="left", padx=5, pady=10)
        tk.Button(frame_top, text="Exportar", width=10).pack(side="left")

        tk.Label(frame_top, text="Pesquisar:").pack(side="left", padx=10)
        self.entry_pesq = tk.Entry(frame_top, width=30)
        self.entry_pesq.pack(side="left")

        tk.Button(frame_top, text="Buscar", command=self.buscar).pack(
            side="left", padx=5)

        tk.Button(frame_top, text="Vendas", width=10).pack(
            side="right", padx=10)

    # ================= TABELA =================
    def criar_tabela(self):
        frame_table = tk.Frame(self.root)
        frame_table.pack(fill="both", expand=True)

        colunas = [
            "codigo", "data_status", "nome", "tipo", "status", "telefone",
            "op_atual", "op_fixo", "op_rec", "setor", "data_vl", "rua", "email", "numero"
        ]

        self.tree = ttk.Treeview(frame_table, columns=colunas, show="headings")

        for col in colunas:
            self.tree.heading(col, text=col.upper())
            self.tree.column(col, width=90)

        self.tree.pack(fill="both", expand=True)

        # Exemplo de dados
        self.tree.insert("", "end", values=(
            44, "06/01/2026", "ROOSEVELT OLIVEIRA", "E", "400", "32419756",
            38, 15, 0, 20, "15/02/2026", "1695", "", 200
        ))

    # ================= PAINEL INFERIOR =================
    def criar_painel_inferior(self):
        frame_bottom = tk.Frame(self.root, height=220)
        frame_bottom.pack(fill="x")

        notebook = ttk.Notebook(frame_bottom)
        notebook.pack(fill="both", expand=True)

        self.criar_aba_recibos(notebook)
        self.criar_aba_boletos(notebook)
        self.criar_aba_cartao(notebook)

    def criar_aba_recibos(self, notebook):
        aba = tk.Frame(notebook)
        notebook.add(aba, text="Recibos")

        cols = ["data", "ligacao", "valor", "flag", "nossonum",
                "status", "operador", "movimento", "data_status", "deposito"]

        tree = ttk.Treeview(aba, columns=cols, show="headings")

        for c in cols:
            tree.heading(c, text=c.upper())
            tree.column(c, width=90)

        tree.pack(fill="both", expand=True)

        tree.insert("", "end", values=(
            "07/01/2026", "06/01/2026", "R$20,00", "Impresso",
            "12475218", "Ent.Prévia", 38, "", "07/01/2026", ""
        ))

    def criar_aba_boletos(self, notebook):
        aba = tk.Frame(notebook)
        notebook.add(aba, text="Boletos/Débito")
        tk.Label(aba, text="Área de boletos/débito").pack(pady=30)

    def criar_aba_cartao(self, notebook):
        aba = tk.Frame(notebook)
        notebook.add(aba, text="Cartão Crédito")
        tk.Label(aba, text="Área de cartão de crédito").pack(pady=30)

    # ================= FUNÇÕES =================
    def buscar(self):
        termo = self.entry_pesq.get()
        messagebox.showinfo("Busca", f"Buscar por: {termo}")


# ================= EXECUÇÃO =================
if __name__ == "__main__":
    root = tk.Tk()
    app = SistemaContribuintes(root)
    root.mainloop()
