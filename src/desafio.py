menu = """
[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair
=> """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:
    opcao = input(menu)

    if opcao == "d":
        valor = float(input("Informe o valor para depositar: "))
        if valor > 0:
            saldo += valor
            extrato += f"Deposito: R$ {valor:.2f}\n"
    elif opcao == "s":
        if LIMITE_SAQUES <= 3:
            valor = float(input("Informe o valor de saque: "))
            if valor > saldo:
                print("Operação falhou! Você não tem saldo suficiente.")

            elif valor > limite:
                print("Operação falhou! O valor do saque excede o limite.")

            elif numero_saques >= LIMITE_SAQUES:
                print("Operação falhou! Número máximo de saques excedido.")
            elif valor > 0:
                saldo -= valor
                extrato += f"Saque: R$ {valor:.2f}\n"
                numero_saques += 1
    elif opcao == "e":
        print("========MOVIMENTAÇÃO BANCÁRIA - EXTRATO========")
        print(extrato)
        print(f"Saldo: {saldo:.2f}")
        print("===============================================")
    elif opcao == "q":
        break

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")