# Convert-PDF-to-frams

### Explicação dos Módulos

1. **tkinter**:  
   - Um módulo padrão em Python para criar interfaces gráficas.
   - Utilizado para criar a janela principal, botões, rótulos e caixas de texto.

2. **filedialog**:  
   - Submódulo do `tkinter` usado para abrir caixas de diálogo que permitem ao usuário selecionar pastas ou ficheiros.

3. **messagebox**:  
   - Submódulo do `tkinter` para exibir mensagens de erro, aviso ou sucesso.

4. **os**:  
   - Módulo padrão para manipular diretórios e caminhos de ficheiros no sistema operativo.

5. **pdf2image**:  
   - Biblioteca que converte PDFs em imagens (frames).
   - Requer a instalação do `poppler-utils` (em sistemas Windows, é necessário baixar o binário Poppler e configurá-lo no PATH).


### Instalação dos Módulos

1. **Instalar o pdf2image**:  
   ```
   pip install pdf2image
   ```

2. **Instalar o Poppler**:  
   - Baixe o Poppler para Windows em [Poppler for Windows](https://github.com/oschwartz10612/poppler-windows).
   - Extraia o conteúdo e adicione o caminho da pasta `bin` às variáveis de ambiente do Windows.

---

### Como Funciona?

1. O usuário seleciona a pasta onde os PDFs estão localizados.
2. O usuário escolhe a pasta onde as imagens serão salvas.
3. Ao clicar em "Converter", o programa processa os PDFs na pasta de entrada e converte cada página em uma imagem, salvando-as na pasta de saída.


### Explicações Adicionais

1. **Barra de Progresso (`ttk.Progressbar`)**:
   - Widget usado para mostrar o progresso da conversão.  
   - O método `["value"]` é atualizado em cada iteração para refletir o progresso atual.

2. **Percentagem do Progresso (`percentagem_var`)**:
   - Mostra o progresso em formato de percentagem.  
   - Calculado como `(número de PDFs processados / total de PDFs) * 100`.

3. **Método `update_idletasks`**:
   - Atualiza a interface gráfica durante loops, garantindo que os elementos visuais (barra de progresso e percentagem) sejam renderizados corretamente.

---

### Como Funciona?
1. O progresso é baseado na quantidade de ficheiros PDF processados.
2. A barra e o texto da percentagem atualizam a cada PDF convertido.
3. Ao finalizar, uma mensagem de sucesso é exibida.

