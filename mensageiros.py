import tkinter as tk
from tkinter import ttk, messagebox


class App:
    def __init__(self, root):
        self.root = root
        self.root.title("Mensageiros")
        self.root.geometry("900x500")

        self.criar_tabela()
        self.criar_botoes()
        self.criar_pesquisa()
        self.carregar_dados_exemplo()

    def criar_tabela(self):
        frame = tk.Frame(self.root)
        frame.pack(fill=tk.BOTH, expand=True, padx=5, pady=5)

        colunas = ("codigo", "mensageiro", "turma",
                   "supervisor", "status", "visivel")

        self.tree = ttk.Treeview(frame, columns=colunas, show="headings")

        self.tree.heading("codigo", text="Código")
        self.tree.heading("mensageiro", text="Mensageiro")
        self.tree.heading("turma", text="Turma")
        self.tree.heading("supervisor", text="Supervisor")
        self.tree.heading("status", text="Status")
        self.tree.heading("visivel", text="Visível")

        self.tree.column("codigo", width=60)
        self.tree.column("mensageiro", width=250)
        self.tree.column("turma", width=60)
        self.tree.column("supervisor", width=150)
        self.tree.column("status", width=60)
        self.tree.column("visivel", width=60)

        scrollbar = ttk.Scrollbar(
            frame, orient="vertical", command=self.tree.yview)
        self.tree.configure(yscrollcommand=scrollbar.set)

        self.tree.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

    def criar_botoes(self):
        frame = tk.Frame(self.root)
        frame.pack(fill=tk.X, padx=5)

        tk.Button(frame, text="Inclusão", width=10,
                  command=self.incluir).pack(side=tk.LEFT, padx=2)
        tk.Button(frame, text="Alteração", width=10,
                  command=self.alterar).pack(side=tk.LEFT, padx=2)
        tk.Button(frame, text="Exclusão", width=10,
                  command=self.excluir).pack(side=tk.LEFT, padx=2)

        tk.Label(frame, text="   ").pack(side=tk.LEFT)

        tk.Button(frame, text="⏮").pack(side=tk.LEFT)
        tk.Button(frame, text="◀").pack(side=tk.LEFT)
        tk.Button(frame, text="▶").pack(side=tk.LEFT)
        tk.Button(frame, text="⏭").pack(side=tk.LEFT)

        tk.Button(frame, text="Saída", width=10,
                  command=self.root.quit).pack(side=tk.RIGHT)

    def criar_pesquisa(self):
        frame = tk.Frame(self.root)
        frame.pack(fill=tk.X, padx=5, pady=5)

        self.tipo_pesquisa = tk.StringVar(value="codigo")

        tk.Radiobutton(frame, text="Código", variable=self.tipo_pesquisa,
                       value="codigo").pack(side=tk.LEFT)
        tk.Radiobutton(frame, text="Nome", variable=self.tipo_pesquisa,
                       value="mensageiro").pack(side=tk.LEFT)
        tk.Radiobutton(frame, text="Ativas", variable=self.tipo_pesquisa,
                       value="status").pack(side=tk.LEFT)

        tk.Label(frame, text="   Pesquisa:").pack(side=tk.LEFT)

        self.entry_pesquisa = tk.Entry(frame, width=30)
        self.entry_pesquisa.pack(side=tk.LEFT, padx=5)

        tk.Button(frame, text="Pesquisar",
                  command=self.pesquisar).pack(side=tk.LEFT)

    def carregar_dados_exemplo(self):
        dados = [
            (1, "DIREÇÃO", 0, "LFA", "I", "V"),
            (2, "MARCILENE CONCEIÇÃO DA SILVA", 0, "LFA", "I", "V"),
            (4, "LAURILANE PEREIRA GOMES", 0, "LFA", "I", "I"),
            (6, "ZENILTO FILHO", 0, "LFA", "I", "V"),
            (10, "BRUNO SANTOS", 0, "VITORIA MELO", "I", "V"),
            (16, "ELANDRO", 0, "VITORIA MELO", "A", "V"),
        ]

        for item in dados:
            self.tree.insert("", tk.END, values=item)

    def incluir(self):
        messagebox.showinfo("Inclusão", "Função de inclusão")

    def alterar(self):
        messagebox.showinfo("Alteração", "Função de alteração")

    def excluir(self):
        messagebox.showinfo("Exclusão", "Função de exclusão")

    def pesquisar(self):
        termo = self.entry_pesquisa.get().lower()
        campo = self.tipo_pesquisa.get()

        for item in self.tree.get_children():
            valores = self.tree.item(item, "values")

            campos = {
                "codigo": str(valores[0]),
                "mensageiro": valores[1].lower(),
                "status": valores[4].lower()
            }

            if termo in campos[campo]:
                self.tree.selection_set(item)
                self.tree.see(item)
                return

        messagebox.showinfo("Pesquisa", "Nenhum resultado encontrado")


if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()
