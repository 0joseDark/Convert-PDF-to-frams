### Como Funciona o Script?

1. **Seleção da Pasta**:
   - O botão "Selecionar" abre uma caixa de diálogo para o utilizador escolher a pasta `bin`.

2. **Adicionar ao PATH**:
   - Verifica se o caminho já está na variável `PATH`.
   - Caso não esteja, usa o comando `setx` do Windows para adicionar o caminho de forma permanente.

3. **Mensagens ao Utilizador**:
   - Utiliza `messagebox` para informar se o caminho foi adicionado com sucesso, já estava presente, ou se ocorreu algum erro.

---

### Explicações Adicionais

1. **Comando `setx`**:
   - É um comando nativo do Windows usado para definir variáveis de ambiente de forma persistente.
   - Alterações feitas com `setx` afetam novas janelas ou programas abertos após a alteração.

2. **Variável PATH**:
   - A variável de ambiente `PATH` contém uma lista de diretórios onde o sistema procura por executáveis.

3. **tkinter**:
   - Biblioteca padrão em Python para criar interfaces gráficas.

---

### Como Testar?

1. Execute o script no seu sistema Windows 10.
2. Escolha a pasta `bin` do Poppler ou de qualquer outro software.
3. Clique em "Adicionar ao PATH" para atualizar a variável `PATH`.
