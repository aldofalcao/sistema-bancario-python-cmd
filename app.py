menu = """
========== SISTEMA BANCÁRIO PROMPT ==========
[D] DEPOSITAR
[S] SACAR
[E] EXTRATO
[Q] SAIR
=============================================
=> """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:
    opcao = input(menu)

    if opcao == "d" or opcao == "D":
        valor = float(input("Informe o valor do depósito: "))

        if valor > 0:
            saldo += valor
            extrato += f"Depósito: R$ {valor:.2f}\n"
        else:
            print("\nOperação falhou! O valor informado é inválido.")
    elif opcao == "s" or opcao == "S":
        valor = float(input("Informe o valor do saque: "))

        excedeu_saldo = valor > saldo
        excedeu_limite = valor > limite
        excedeu_saques = numero_saques >= LIMITE_SAQUES

        if excedeu_saldo:
            print("\nOperação falhou! Você não tem saldo sufuciente.")
        elif excedeu_limite:
            print("\nOperação falhou! O valor do saque excedeu o limite.")
        elif excedeu_saques:
            print("\nOperação falhou! Número máximo de saques excedido.")
        elif valor > 0:
            saldo -= valor
            extrato += f"Saque: R$ {valor:.2f}\n"
            numero_saques += 1
        else:
            print("\nOperação falhou! O valor informado é inválido.")
    elif opcao == "e" or opcao == "E":
            print("\n=============== EXTRATO =====================")
            print("Não foram realizadas movimentações." if not extrato else extrato)
            print(f"\nSaldo: R$ {saldo:.2f}")
            print("=============================================")
    elif opcao == "q" or opcao == "Q":
        break
    else:
        print("\nOperação inválida, por favor selecione a operação desejada.")
