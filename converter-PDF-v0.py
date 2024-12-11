import tkinter as tk
from tkinter import filedialog, messagebox
from tkinter import ttk
import os
import pdfplumber
import markdown

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

# Função para converter PDFs em Markdown
def converter_pdf_em_markdown():
    pasta_entrada = entrada_var.get()
    pasta_saida = saida_var.get()

    if not pasta_entrada or not pasta_saida:
        messagebox.showerror("Erro", "Por favor, selecione as pastas de entrada e saída.")
        return

    # Listar apenas arquivos PDF
    pdfs = [f for f in os.listdir(pasta_entrada) if f.endswith(".pdf")]

    if not pdfs:
        messagebox.showwarning("Aviso", "Nenhum arquivo PDF encontrado na pasta de entrada.")
        return

    progresso_bar["maximum"] = len(pdfs)
    progresso_bar["value"] = 0

    try:
        for index, ficheiro in enumerate(pdfs):
            caminho_pdf = os.path.join(pasta_entrada, ficheiro)
            caminho_md = os.path.join(pasta_saida, f"{os.path.splitext(ficheiro)[0]}.md")

            with pdfplumber.open(caminho_pdf) as pdf:
                texto = ""
                for pagina in pdf.pages:
                    extraido = pagina.extract_text()
                    if extraido:  # Verificar se o texto foi extraído
                        texto += extraido + "\n"

            if texto.strip():
                # Converter texto para Markdown e salvar
                markdown_texto = markdown.markdown(texto)
                with open(caminho_md, "w", encoding="utf-8") as ficheiro_md:
                    ficheiro_md.write(markdown_texto)
            else:
                messagebox.showwarning("Aviso", f"Não foi possível extrair texto do PDF: {ficheiro}")

            progresso_bar["value"] = index + 1
            percentagem_var.set(f"{int((index + 1) / len(pdfs) * 100)}%")
            janela.update_idletasks()

        messagebox.showinfo("Sucesso", "Conversão concluída com sucesso!")
    except Exception as e:
        # Capturar erros e informar ao usuário
        messagebox.showerror("Erro", f"Ocorreu um erro durante a conversão: {e}")

# Janela principal
janela = tk.Tk()
janela.title("Conversor de PDF para Markdown")

# Variáveis para armazenar os caminhos
entrada_var = tk.StringVar()
saida_var = tk.StringVar()
percentagem_var = tk.StringVar(value="0%")

# Rótulos e entradas
tk.Label(janela, text="Caminho da Pasta de Entrada:").grid(row=0, column=0, sticky="w", padx=5, pady=5)
tk.Entry(janela, textvariable=entrada_var, width=50).grid(row=0, column=1, padx=5, pady=5)
tk.Button(janela, text="Selecionar", command=selecionar_pasta_entrada).grid(row=0, column=2, padx=5, pady=5)

tk.Label(janela, text="Caminho da Pasta de Saída:").grid(row=1, column=0, sticky="w", padx=5, pady=5)
tk.Entry(janela, textvariable=saida_var, width=50).grid(row=1, column=1, padx=5, pady=5)
tk.Button(janela, text="Selecionar", command=selecionar_pasta_saida).grid(row=1, column=2, padx=5, pady=5)

# Botão de conversão
tk.Button(janela, text="Converter", command=converter_pdf_em_markdown).grid(row=2, column=1, pady=10)

# Barra de progresso
progresso_bar = ttk.Progressbar(janela, length=400, mode="determinate")
progresso_bar.grid(row=3, column=1, pady=10)

# Label para mostrar a percentagem
tk.Label(janela, textvariable=percentagem_var).grid(row=4, column=1, pady=5)

# Botão de sair
tk.Button(janela, text="Sair", command=janela.quit).grid(row=5, column=1, pady=10)

# Loop principal da aplicação
janela.mainloop()
