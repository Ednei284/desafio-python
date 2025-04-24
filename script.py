menu = """

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair


=> """
saldo = 0
extrato = ""
limite = 500
numero_de_saques = 0
limite_de_saques = 3
try:
    while True:
        option = input(menu).strip().lower()
        if option == "d":
            valor = float(input("Digite o valor a ser depositado: "))
            if valor > 0:
                saldo += valor
                extrato += f"Depósito: R$ {valor:.2f}\n"
            else:
                print("Valor inválido!")
        elif option == "s":
            valor = float(input("Digite o valor a ser sacado: "))
            excedeu_saldo = valor > saldo
            excedeu_limite = valor > limite
            excedeu_saques = numero_de_saques >= limite_de_saques

            if excedeu_saldo:
                print("Você não tem saldo suficiente.")
            elif excedeu_limite:
                print("Você não pode sacar mais que R$ 500,00.")
            elif excedeu_saques:
                print("Número máximo de saques atingido.")
            elif valor > 0:
                saldo -= valor
                extrato += f"Saque: R$ {valor:.2f}\n"
                numero_de_saques += 1
            else:
                print("Valor inválido!")
        elif option == "e":
            print("\n================= EXTRATO =================")
            print(extrato if extrato else "Não foram realizadas movimentações.")
            print(f"\nSaldo disponível: R$ {saldo:.2f}")
            print("=============================================")
        elif option == "q":
            break
        else:
            print("Opção inválida!")
except KeyboardInterrupt:
    print("\nPrograma encerrado pelo usuário.")