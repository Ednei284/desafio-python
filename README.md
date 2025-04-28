# Desafio Python Suzano

Este projeto contém um script Python (`script.py`) desenvolvido como parte do desafio proposto pela DIO. Abaixo, você encontrará informações sobre o propósito do script, como utilizá-lo e os requisitos necessários para sua execução.

## Objetivo

O script foi criado para simular uma interface bancária para cliente. Ele foi projetado para ser simples de usar e eficiente.

## Como usar

1. Certifique-se de ter o Python instalado em sua máquina (versão 3.x ou superior).
2. Clone este repositório ou faça o download do arquivo `script.py`.
3. Navegue até o diretório onde o arquivo está localizado.
4. Execute o script com o comando `python` ou `python3` dependendo do alias do seu S.O:
   ```bash
   python script.py
   ```
5. Siga as instruções exibidas no terminal.

## Requisitos

- Python 3.x

## Estrutura do Código

O script está organizado da seguinte forma:

- **Funções principais**: Depósito, Saque, Extrato e Sair
- **Entrada e saída**: O sistema recebe um número e devolve uma mensagem após fazer a operação
- **Validação de entradas**:
  - O sistema valida se o usuário inseriu um número válido ao realizar depósitos ou saques.
  - Caso o usuário insira letras ou caracteres inválidos, o programa exibe uma mensagem de erro e solicita o valor novamente.
- **Limite de transações diárias**:
  - O sistema limita o número de transações diárias a 10 (entre depósitos e saques).
  - Caso o limite seja atingido, o programa informa o usuário e impede novas transações.
- **Exemplo de execução**:
  ```bash
  python script.py

  ```

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=>

```

## Contribuição

Contribuições são bem-vindas! Sinta-se à vontade para abrir issues ou enviar pull requests.

## Licença

Este projeto está licenciado sob a licença [MIT](LICENSE).
```
