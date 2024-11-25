import tkinter as tk
from tkinter import filedialog, messagebox
from pdf2image import convert_from_path
import os

# Função para selecionar a pasta de entrada
def selecionar_pasta_entrada():
    pasta = filedialog.askdirectory(title="Selecionar Pasta de Entrada")
    if pasta:
        entrada_var.set(pasta)

# Função para selecionar a pasta de saída
def selecionar_pasta_saida():
    pasta = filedialog.askdirectory(title="Selecionar Pasta de Saída")
    if pasta:
        saida_var.set(pasta)

# Função para converter PDFs em frames (imagens)
def converter_pdf_em_frames():
    pasta_entrada = entrada_var.get()
    pasta_saida = saida_var.get()

    if not pasta_entrada or not pasta_saida:
        messagebox.showerror("Erro", "Por favor, selecione as pastas de entrada e saída.")
        return

    try:
        for ficheiro in os.listdir(pasta_entrada):
            if ficheiro.endswith(".pdf"):
                caminho_pdf = os.path.join(pasta_entrada, ficheiro)
                imagens = convert_from_path(caminho_pdf)

                # Salvar cada página como uma imagem
                for i, imagem in enumerate(imagens):
                    nome_imagem = f"{os.path.splitext(ficheiro)[0]}_pagina_{i + 1}.jpg"
                    caminho_imagem = os.path.join(pasta_saida, nome_imagem)
                    imagem.save(caminho_imagem, "JPEG")

        messagebox.showinfo("Sucesso", "Conversão concluída com sucesso!")
    except Exception as e:
        messagebox.showerror("Erro", f"Ocorreu um erro: {e}")

# Janela principal
janela = tk.Tk()
janela.title("Conversor de PDF para Frames")

# Variáveis para armazenar os caminhos
entrada_var = tk.StringVar()
saida_var = tk.StringVar()

# Rótulos e entradas
tk.Label(janela, text="Caminho da Pasta de Entrada:").grid(row=0, column=0, sticky="w", padx=5, pady=5)
tk.Entry(janela, textvariable=entrada_var, width=50).grid(row=0, column=1, padx=5, pady=5)
tk.Button(janela, text="Selecionar", command=selecionar_pasta_entrada).grid(row=0, column=2, padx=5, pady=5)

tk.Label(janela, text="Caminho da Pasta de Saída:").grid(row=1, column=0, sticky="w", padx=5, pady=5)
tk.Entry(janela, textvariable=saida_var, width=50).grid(row=1, column=1, padx=5, pady=5)
tk.Button(janela, text="Selecionar", command=selecionar_pasta_saida).grid(row=1, column=2, padx=5, pady=5)

# Botão de conversão
tk.Button(janela, text="Converter", command=converter_pdf_em_frames).grid(row=2, column=1, pady=10)

# Botão de sair
tk.Button(janela, text="Sair", command=janela.quit).grid(row=3, column=1, pady=10)

# Loop principal da aplicação
janela.mainloop()
