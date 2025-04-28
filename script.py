from datetime import date

menu = """

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair ou CRTL + C para sair
Escolha uma opção: 

=> """
saldo = 0
extrato = ""
limite = 500
numero_de_saques = 0
limite_de_saques = 3
transacoes = 0
data_atual = date.today()
data_formatada = data_atual.strftime("%d/%m/%Y")
try:
    while True:
        option = input(menu).strip().lower()
        if option == "d":
            if transacoes == 10 and data_atual:
                print("Você atingiu o limite de 10 transações por dia.")
                continue
            while True:
                try:
                    valor = float(input("Digite o valor a ser depositado: "))
                    if valor > 0:
                        saldo += valor
                        extrato += f"Depósito: R$ {valor:.2f} data: {data_atual}\n"
                        transacoes += 1
                        print(transacoes)
                        break
                    else:
                        print("Valor inválido!")
                except ValueError:
                    print("Valor inválido!")
        elif option == "s":
            if transacoes == 10 and data_atual:
                print("Você atingiu o limite de 10 transações por dia.")
                continue
            while True:
                try:
                    valor = float(input("Digite o valor a ser sacado: "))
                    if valor > saldo:
                        print("Valor maior que o saldo disponível!")
                    elif valor > limite:
                        print("Valor maior que o limite de saque!")
                    elif numero_de_saques >= limite_de_saques:
                        print("Número máximo de saques atingido!")
                    elif valor <= 0:
                        print("Valor inválido!")
                    else:
                        saldo -= valor
                        extrato += f"Saque: R$ {valor:.2f} data: {data_atual}\n"
                        numero_de_saques += 1
                        transacoes += 1
                        print(transacoes)
                        break
                except ValueError:
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
