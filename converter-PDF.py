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
                    texto += pagina.extract_text() + "\n"

            # Converter texto para Markdown e
