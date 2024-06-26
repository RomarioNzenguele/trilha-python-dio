def menu():
    return """
[d] Depositar
[s] Sacar
[t] Transferir
[p] Pagar Conta
[e] Extrato
[q] Sair

=> """


def depositar(saldo, extrato):
    valor = float(input("Informe o valor do depósito: "))
    if valor > 0:
        saldo += valor
        extrato += f"Depósito: R$ {valor:.2f}\n"
    else:
        print("Operação falhou! O valor informado é inválido.")
    return saldo, extrato


def sacar(saldo, extrato, numero_saques, limite, LIMITE_SAQUES):
    valor = float(input("Informe o valor do saque: "))
    excedeu_saldo = valor > saldo
    excedeu_limite = valor > limite
    excedeu_saques = numero_saques >= LIMITE_SAQUES

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
    else:
        print("Operação falhou! O valor informado é inválido.")

    return saldo, extrato, numero_saques


def transferir(saldo, extrato, historico_transferencias):
    valor = float(input("Informe o valor da transferência: "))
    excedeu_saldo = valor > saldo

    if excedeu_saldo:
        print("Operação falhou! Você não tem saldo suficiente.")
    elif valor > 0:
        conta_destino = input("Informe o número da conta de destino: ")
        saldo -= valor
        historico_transferencias += f"Transferência de R$ {valor:.2f} para a conta {conta_destino}\n"
        extrato += f"Transferência: R$ {valor:.2f}\n"
    else:
        print("Operação falhou! O valor informado é inválido.")

    return saldo, extrato, historico_transferencias


def pagar_conta(saldo, extrato, historico_pagamentos):
    valor = float(input("Informe o valor do pagamento: "))
    excedeu_saldo = valor > saldo

    if excedeu_saldo:
        print("Operação falhou! Você não tem saldo suficiente.")
    elif valor > 0:
        descricao = input("Informe a descrição do pagamento: ")
        saldo -= valor
        historico_pagamentos += f"Pagamento de R$ {valor:.2f} para {descricao}\n"
        extrato += f"Pagamento: R$ {valor:.2f}\n"
    else:
        print("Operação falhou! O valor informado é inválido.")

    return saldo, extrato, historico_pagamentos


def mostrar_extrato(saldo, extrato):
    print("\n================ EXTRATO ================")
    if not extrato:
        print("Não foram realizadas movimentações.")
    else:
        print(extrato)
    print(f"\nSaldo: R$ {saldo:.2f}")
    print("==========================================")


def main():
    saldo = 0
    limite = 500
    extrato = ""
    numero_saques = 0
    LIMITE_SAQUES = 3
    historico_transferencias = ""
    historico_pagamentos = ""

    while True:
        opcao = input(menu())

        if opcao == "d":
            saldo, extrato = depositar(saldo, extrato)
        elif opcao == "s":
            saldo, extrato, numero_saques = sacar(saldo, extrato, numero_saques, limite, LIMITE_SAQUES)
        elif opcao == "t":
            saldo, extrato, historico_transferencias = transferir(saldo, extrato, historico_transferencias)
        elif opcao == "p":
            saldo, extrato, historico_pagamentos = pagar_conta(saldo, extrato, historico_pagamentos)
        elif opcao == "e":
            mostrar_extrato(saldo, extrato)
        elif opcao == "q":
            break
        else:
            print("Operação inválida, por favor selecione novamente a operação desejada.")


if __name__ == "__main__":
    main()
