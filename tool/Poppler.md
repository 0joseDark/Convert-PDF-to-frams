O **Poppler** é uma biblioteca poderosa para manipulação de arquivos PDF, usada em conjunto com o módulo **pdf2image** para converter PDFs em imagens (frames). No Windows, o **Poppler** precisa ser instalado separadamente porque ele não faz parte da instalação padrão do Python nem está nativamente disponível no sistema operacional.

### Por que o Poppler é necessário?
1. **Renderização de PDFs**:
   - O módulo **pdf2image** não realiza a renderização diretamente. Ele utiliza o Poppler para interpretar e converter o conteúdo das páginas do PDF em imagens.

2. **Suporte a PDFs Complexos**:
   - Muitos PDFs incluem gráficos vetoriais, fontes embutidas e camadas que requerem ferramentas avançadas para renderizar corretamente. O Poppler é otimizado para lidar com esses casos.

3. **Compatibilidade**:
   - O Poppler é amplamente utilizado porque funciona em várias plataformas e suporta diferentes formatos de saída (como JPEG, PNG e outros).

---

### Como instalar o Poppler no Windows

1. **Descarregar o Poppler**:
   - Faça o download de uma versão compilada do Poppler para Windows a partir do site oficial ou de repositórios confiáveis, como:
     - [Poppler para Windows - GitHub](https://github.com/oschwartz10612/poppler-windows/releases/)

2. **Extrair os Arquivos**:
   - Extraia os ficheiros do Poppler para uma pasta no seu computador, como `C:\Program Files\poppler`.

3. **Adicionar à Variável PATH**:
   - Adicione o caminho da pasta `bin` do Poppler (`C:\Program Files\poppler\bin`) à variável de ambiente `PATH`. Isso permite que o sistema encontre os executáveis do Poppler necessários para o **pdf2image**.

---

### Configurar o Módulo `pdf2image`

1. Instale o **pdf2image** usando `pip`:
   ```bash
   pip install pdf2image
   ```

2. Verifique se o Poppler está configurado corretamente:
   - O **pdf2image** procura automaticamente pelo Poppler no `PATH`.
   - Se o Poppler não estiver no `PATH`, pode ser necessário especificar o caminho diretamente no seu script Python:
     ```python
     from pdf2image import convert_from_path

     # Caminho para o executável do Poppler
     caminho_poppler = r"C:\Program Files\poppler\bin"

     # Converte o PDF em imagens
     imagens = convert_from_path("documento.pdf", poppler_path=caminho_poppler)
     ```

---

### Por que o Poppler é Essencial para o Conversor?

Sem o Poppler:
- O módulo **pdf2image** não funcionará, gerando erros ao tentar converter arquivos PDF.
- A conversão para imagens (frames) não será possível.

Com o Poppler:
- O programa pode abrir e converter qualquer PDF em imagens.
- O utilizador pode salvar cada página do PDF como uma imagem separada (em formato como `.jpeg` ou `.png`).

---

### Resumo do Processo

1. Instale o **Poppler** no Windows.
2. Adicione o caminho da pasta `bin` do Poppler às variáveis de ambiente do Windows ou especifique o caminho diretamente no código.
3. Instale e use o **pdf2image** para realizar a conversão de PDFs em imagens com a ajuda do Poppler.
