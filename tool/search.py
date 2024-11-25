from pdf2image import convert_from_path

# Caminho para o executável do Poppler
caminho_poppler = r"C:\Program Files\poppler\bin"

# Converte o PDF em imagens
imagens = convert_from_path("documento.pdf", poppler_path=caminho_poppler)
