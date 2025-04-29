# Desafio Python Suzano

Este projeto contém um script Python (`script.py`) desenvolvido como parte do desafio proposto pela DIO. Abaixo, você encontrará informações sobre o propósito do script, como utilizá-lo e os requisitos necessários para sua execução.

## Objetivo

O script foi criado para simular uma interface bancária para clientes. Ele foi projetado para ser simples de usar e eficiente.

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

- **Funções principais**:

  - **Depósito**: Permite ao usuário depositar um valor na conta. Valida se o valor é positivo.
  - **Saque**: Permite ao usuário sacar um valor da conta. Valida:
    - Se o valor não excede o saldo disponível.
    - Se o valor não excede o limite de saque por transação (R$ 500,00).
    - Se o número máximo de saques diários (3) não foi atingido.
  - **Extrato**: Exibe todas as transações realizadas (depósitos e saques) e o saldo atual.
  - **Criar Usuário**: Permite cadastrar novos usuários com informações como CPF, nome, data de nascimento e endereço. Valida se o CPF já está cadastrado.
  - **Criar Conta**: Permite criar contas bancárias associadas a usuários existentes. Cada conta é identificada por um número único e vinculada a uma agência.
  - **Listar Contas**: Exibe todas as contas cadastradas, incluindo informações como agência, número da conta e nome do usuário.
  - **Sair**: Permite encerrar o programa.

- **Validação de entradas**:

  - O sistema valida se o usuário inseriu um número válido ao realizar depósitos ou saques.
  - Caso o usuário insira letras ou caracteres inválidos, o programa exibe uma mensagem de erro e solicita o valor novamente.

- **Limite de transações diárias**:
  - O sistema limita o número de transações diárias a 10 (entre depósitos e saques).
  - Caso o limite seja atingido, o programa informa o usuário e impede novas transações.

## Exemplo de execução

```plaintext
[d] Depositar
[s] Sacar
[e] Extrato
[nc] Nova conta
[lc] Listar contas
[nu] Novo usuário
[q] Sair ou CTRL + C para sair

=> d
Digite o valor a ser depositado: 100
Depósito realizado com sucesso!

=> s
Digite o valor a ser sacado: 50
Saque realizado com sucesso!

=> e
================ EXTRATO ================
Depósito: R$ 100.00
Saque: R$ 50.00

Saldo: R$ 50.00
=========================================
```

## Contribuição

Contribuições são bem-vindas! Sinta-se à vontade para abrir issues ou enviar pull requests.

## Licença

Este projeto está licenciado sob a licença [MIT](LICENSE).
