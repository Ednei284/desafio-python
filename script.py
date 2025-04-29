import textwrap


def menu():
    menu = """\n
    ============== MENU ============
    [d]\t Depositar
    [s]\t Sacar
    [e]\t Extrato
    [nc]\t Nova conta
    [lc]\t Listar contas
    [nu]\t novo usuário
    [q]\t Sair ou CRTL + C para sair
    Escolha uma opção: 

    => """
    return input(textwrap.dedent(menu))


def depositar(saldo, valor, extrato, /):
    if valor > 0:
        saldo += valor
        extrato += f"Depósito: R$ {valor:.2f}\n"
        print("Depósito realizado com sucesso.")

    else:
        print("Valor inválido para depósito.")
    return saldo, extrato


def sacar(*, saldo, valor, extrato, limite, numero_saques, limite_saque):
    excedeu_saldo = valor > saldo
    excedeu_limite = valor > limite
    excedeu_saques = numero_saques >= limite_saque
    if excedeu_saldo:
        print("Operação falhou! Você não tem saldo suficiente.")
    elif excedeu_limite:
        print("Operação falhou! O valor do saque excede o limite.")
    elif excedeu_saques:
        print("Operação falhou! Número máximo de saques excedido.")
    elif valor > 0:
        saldo -= valor
        extrato += f"Saque: R$ {valor:.2f}\n"
        numero_saques += 1
        print("Saque realizado com sucesso.")
    else:
        print("Valor inválido para saque.")
    return saldo, extrato


def exibir_extrato(saldo, /, *, extrato):
    print("\n================ EXTRATO ================")
    print("Não foram realizadas movimentações." if not extrato else extrato)
    print(f"\nSaldo: R$ {saldo:.2f}")
    print("==========================================")


def criar_usuario(usuarios):
    cpf = input("Informe o CPF (somente números): ")
    usuario = filtrar_usuario(cpf, usuarios)
    if usuario:
        print("Já existe um usuário com esse CPF!")
        return
    nome = input("Informe o nome completo: ")
    data_nascimento = input("Informe a data de nascimento (dd-mm-aaaa): ")
    endereco = input("Informe o endereço (logradouro, número - bairro): ")
    usuarios.append(
        {
            "nome": nome,
            "data_nascimento": data_nascimento,
            "cpf": cpf,
            "endereco": endereco,
        }
    )
    print("Usuário cadastrado com sucesso!")


def filtrar_usuario(cpf, usuarios):
    usuarios_filtrados = [usuario for usuario in usuarios if usuario["cpf"] == cpf]
    return usuarios_filtrados[0] if usuarios_filtrados else None


def listar_contas(contas):
    for conta in contas:
        linha = f"""\n
              Agência:\t {conta['agencia']} 
              Conta:\t {conta['numero_conta']} 
              Usuário:\t {conta['usuario']['nome']}
        """
        print("=" * 100)
        print(textwrap.dedent(linha))


def criar_conta(agencia, numero_conta, usuarios):
    cpf = input("Informe o CPF do usuário: ")
    usuario = filtrar_usuario(cpf, usuarios)
    if usuario:
        return {
            "agencia": agencia,
            "numero_conta": numero_conta,
            "usuario": usuario,
        }
    print("Usuário não encontrado!")


def main():
    LIMITE_SAQUE = 3
    AGENCIA = "0001"

    saldo = 0
    limite = 500
    extrato = ""
    numero_saques = 0
    usuarios = []
    contas = []

    try:
        while True:
            option = menu()
            if option == "d":
                try:
                    valor = float(input("Digite o valor a ser depositado: "))
                    saldo, extrato = depositar(saldo, valor, extrato)
                except ValueError:
                    print("Valor inválido!")
            elif option == "s":
                try:
                    valor = float(input("Digite o valor a ser sacado: "))
                    saldo, extrato = sacar(
                        saldo=saldo,
                        valor=valor,
                        extrato=extrato,
                        limite=limite,
                        numero_saques=numero_saques,
                        limite_saque=LIMITE_SAQUE,
                    )
                except ValueError:
                    print("Valor inválido!")
            elif option == "e":
                exibir_extrato(saldo, extrato=extrato)
            elif option == "nu":
                criar_usuario(usuarios)
            elif option == "nc":
                numero_conta = len(contas) + 1
                conta = criar_usuario(AGENCIA, numero_conta, usuarios)
                if conta:
                    contas.append(conta)
                    print("Conta criada com sucesso!")
            elif option == "lc":
                listar_contas(contas)
            elif option == "q":
                break
            else:
                print("Opção inválida!")
    except KeyboardInterrupt:
        print("\nPrograma encerrado pelo usuário.")
