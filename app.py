import tkinter as tk
from tkinter import ttk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure

# ---------------- JANELA PRINCIPAL ----------------
root = tk.Tk()
root.title("Telemarketing - Sistema de Produção")
root.geometry("1200x700")

# ---------------- MENU ----------------
menu_bar = tk.Menu(root)

# Menu Cadastros
menu_cadastros = tk.Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="Cadastros", menu=menu_cadastros)
menu_cadastros.add_command(label="Contribuintes")
menu_cadastros.add_separator()
menu_cadastros.add_command(label="Recibos")
menu_cadastros.add_command(label="Boletos")
menu_cadastros.add_command(label="Cobrança")
menu_cadastros.add_separator()
menu_cadastros.add_command(label='Operadores')
menu_cadastros.add_command(label="Mensageiros")
menu_cadastros.add_command(label="Superviores")
menu_cadastros.add_separator()
menu_cadastros.add_command(label="Ruas")
menu_cadastros.add_command(label="Setores")
menu_cadastros.add_command(label="E-mail")

# ------------------------------------------------------

# Menu Consultas
menu_consultas = tk.Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="Consultas", menu=menu_consultas)
menu_consultas.add_command(label="Recibos")
menu_consultas.add_command(label="Boletos/Débitos/Cartão")
menu_consultas.add_separator()
menu_consultas.add_command(label='Operadores')
menu_consultas.add_command(label="Mensageiros")
menu_consultas.add_separator()
menu_consultas.add_command(label="Eventos do Recibo")
menu_consultas.add_command(label="Gerencial p/Valor")


# ---------------------------------------------------------

# Menu Impressão
menu_impressao = tk.Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="Impressão", menu=menu_impressao)
menu_impressao.add_command(label="Recibos")
menu_impressao.add_command(label="Relatórios")
menu_impressao.add_command(label="GeradorSqlDinamico")

# -------------------------------------------------------------

# Menu Opções
menu_opcoes = tk.Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="Opções", menu=menu_opcoes)
menu_opcoes.add_command(label="Cobrança de Recibos")
menu_opcoes.add_command(label="Cobrança de Boletos")
menu_opcoes.add_separator()
menu_opcoes.add_command(label="Gera Repique")
menu_opcoes.add_command(label="Troca DIstribuição")
menu_opcoes.add_command(label='Troca Status Contribuite')
menu_opcoes.add_command(label="Controle Escelsa")
menu_opcoes.add_command(label="Excel")
menu_opcoes.add_command(label="Campanha Extra")
menu_opcoes.add_command(label="Bancos")
menu_opcoes.add_command(label="Cartão de Crédito")
menu_opcoes.add_command(label="Rota")
menu_opcoes.add_command(label="Gera Boletos para Inadimplentes")
menu_opcoes.add_command(label="Registra Boletos na iugu")

# -----------------------------------------------------------------

# Menu Tabelas
menu_tabelas = tk.Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="Tabelas", menu=menu_tabelas)
menu_tabelas.add_command(label="Status")
menu_tabelas.add_command(label="Parâmetros")
menu_tabelas.add_separator()
menu_tabelas.add_command(label="Gurpo de Usuários")
menu_tabelas.add_command(label='Niveis de Acesso')
menu_tabelas.add_separator()
menu_tabelas.add_command(label="Itens")
menu_tabelas.add_command(label="Fluxo de Caixa")
menu_tabelas.add_command(label="Produtos")
menu_tabelas.add_command(label="Tipo de Pagamentos")
menu_tabelas.add_command(label="Feriados")

# ------------------------------------------------------------------

# Menu Utilitários
menu_utilitarios = tk.Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="Utilitários", menu=menu_utilitarios)
menu_utilitarios.add_command(label="Pârametros do Sistema")
menu_utilitarios.add_command(label="SitiWeb")
menu_utilitarios.add_separator()
menu_utilitarios.add_command(label="Auditoria")
menu_utilitarios.add_command(label='Importa Arquivo Ruas dos Correios')
menu_utilitarios.add_command(label="Listagem Voltar Backup - 3")
menu_utilitarios.add_command(label="Atualiza Intervalo")
menu_utilitarios.add_separator()
menu_utilitarios.add_command(label="Mudança de Usuário")
menu_utilitarios.add_command(label="Troca Senha")
menu_utilitarios.add_command(label="Caixa Postal")
menu_utilitarios.add_separator()
menu_utilitarios.add_command(label="Backup")
menu_utilitarios.add_command(label='Atualização do Software')
menu_utilitarios.add_command(label="Solicitar Manuntenção AnyDesk")
menu_utilitarios.add_command(label="Solicitar Manuntenção TeamViewer")
menu_utilitarios.add_command(label="Reconectar ao Banco de Dados")
menu_utilitarios.add_command(label="Ticket")
menu_utilitarios.add_command(label="Gerar Dados Estatisticos")
menu_utilitarios.add_command(label="Sobre")
menu_utilitarios.add_separator()
menu_utilitarios.add_command(label="Fechar", command=menu_bar.quit)

# ------------------------------------------------------------------

root.config(menu=menu_bar)

# ---------------- BARRA SUPERIOR ----------------
top_frame = ttk.Frame(root)
top_frame.pack(fill="x", padx=10, pady=5)

# btn_fechar = tk.Button(root, text="Sair", command=root.destroy)
# btn_fechar.pack(pady=10)


buttons = [
    "Contribuintes",
    "Recibos",
    "Bol/Deb/Car",
    "Operadores",
    "Mensageiros",
    "Supervisores",
    "Ruas",
    "Setores",
    "Usuários",
    "Listagem",
]


for btn in buttons:
    ttk.Button(top_frame, text=btn).pack(side="left", padx=5)

# ---------------- ÁREA DE GRÁFICOS ----------------
content = ttk.Frame(root)
content.pack(fill="both", expand=True)

left_frame = ttk.Frame(content)
left_frame.pack(side="left", fill="both", expand=True)

right_frame = ttk.Frame(content)
right_frame.pack(side="right", fill="both", expand=True)

# ---------------- GRÁFICO 1 ----------------
fig1 = Figure(figsize=(4, 3), dpi=100)
ax1 = fig1.add_subplot(111)

meta = 50
producao = 40.75

ax1.bar(["Meta", "Produção"], [meta, producao], color=["blue", "red"])
ax1.set_title("Meta de Produção - Média por Ficha")

canvas1 = FigureCanvasTkAgg(fig1, master=left_frame)
canvas1.draw()
canvas1.get_tk_widget().pack(fill="both", expand=True)

# ---------------- GRÁFICO 2 ----------------
fig2 = Figure(figsize=(4, 3), dpi=100)
ax2 = fig2.add_subplot(111)

dias = ["30/12", "05/01"]
valores = [3781, 8041]

ax2.bar(dias, valores, color="red")
ax2.set_title("Produção - Últimos Dias")

canvas2 = FigureCanvasTkAgg(fig2, master=right_frame)
canvas2.draw()
canvas2.get_tk_widget().pack(fill="both", expand=True)

# ---------------- STATUS BAR ----------------
status = ttk.Label(
    root,
    text="Usuário: VITÓRIA MARIA | terça-feira, 06 de janeiro de 2026",
    relief="sunken",
    anchor="w"
)
status.pack(side="bottom", fill="x")

# ---------------- EXECUÇÃO ----------------
root.mainloop()
