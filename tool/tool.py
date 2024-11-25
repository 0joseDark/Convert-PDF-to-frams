import os
import tkinter as tk
from tkinter import filedialog, messagebox

def selecionar_pasta():
    """Abre uma caixa de diálogo para o utilizador selecionar uma pasta."""
    pasta = filedialog.askdirectory(title="Selecionar Pasta bin")
    if pasta:
        caminho_var.set(pasta)

def adicionar_ao_path():
    """Adiciona o caminho selecionado às variáveis de ambiente do Windows."""
    caminho = caminho_var.get()

    if not caminho:
        messagebox.showerror("Erro", "Por favor, selecione uma pasta.")
        return

    try:
        # Obtém o PATH atual
        path_atual = os.environ.get("PATH", "")

        # Adiciona o caminho ao PATH se ainda não estiver presente
        if caminho not in path_atual:
            os.system(f'setx PATH "{path_atual};{caminho}"')
            messagebox.showinfo("Sucesso", f"A pasta '{caminho}' foi adicionada ao PATH!")
        else:
            messagebox.showinfo("Informação", f"A pasta '{caminho}' já está no PATH.")
    except Exception as e:
        messagebox.showerror("Erro", f"Ocorreu um erro ao adicionar ao PATH: {e}")

# Janela principal
janela = tk.Tk()
janela.title("Adicionar Pasta bin ao PATH")

# Variável para armazenar o caminho da pasta
caminho_var = tk.StringVar()

# Layout
tk.Label(janela, text="Caminho da Pasta bin:").grid(row=0, column=0, padx=5, pady=5, sticky="w")
tk.Entry(janela, textvariable=caminho_var, width=50).grid(row=0, column=1, padx=5, pady=5)
tk.Button(janela, text="Selecionar", command=selecionar_pasta).grid(row=0, column=2, padx=5, pady=5)

tk.Button(janela, text="Adicionar ao PATH", command=adicionar_ao_path).grid(row=1, column=1, pady=10)
tk.Button(janela, text="Sair", command=janela.quit).grid(row=2, column=1, pady=10)

# Loop principal da aplicação
janela.mainloop()
