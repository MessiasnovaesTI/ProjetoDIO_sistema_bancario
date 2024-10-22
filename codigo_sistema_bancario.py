saldo = 0.0
limite_saque = 500.0
limite_saques_diarios = 3
numero_saques = 0
extrato = []

def depositar(valor):
    global saldo
    if valor > 0:
        saldo += valor
        extrato.append(f"Depósito: R$ {valor:.2f}")
        print(f"Depósito de R$ {valor:.2f} realizado com sucesso!")
    else:
        print("Operação inválida. O valor do depósito deve ser positivo.")

def sacar(valor):
    global saldo
    global numero_saques

    if numero_saques >= limite_saques_diarios:
        print("Limite de saques diários atingido.")
    elif valor > limite_saque:
        print(f"O limite por saque é de R$ {limite_saque:.2f}.")
    elif valor > saldo:
        print("Saldo insuficiente.")
    elif valor > 0:
        saldo -= valor
        numero_saques += 1
        extrato.append(f"Saque: R$ {valor:.2f}")
        print(f"Saque de R$ {valor:.2f} realizado com sucesso!")
    else:
        print("Operação inválida. O valor do saque deve ser positivo.")

def visualizar_extrato():
    print("\nExtrato:")
    if not extrato:
        print("Não foram realizadas movimentações.")
    else:
        for movimento in extrato:
            print(movimento)
        print(f"\nSaldo atual: R$ {saldo:.2f}")

def menu():
    print("\n=== Sistema Bancário ===")
    print("1. Depósito")
    print("2. Saque")
    print("3. Extrato")
    print("4. Sair")
    
    opcao = input("Escolha uma opção: ")
    return opcao

while True:
    opcao = menu()
    
    if opcao == "1":
        valor = float(input("Digite o valor do depósito: "))
        depositar(valor)
    
    elif opcao == "2":
        valor = float(input("Digite o valor do saque: "))
        sacar(valor)
    
    elif opcao == "3":
        visualizar_extrato()
    
    elif opcao == "4":
        print("Saindo do sistema bancário...")
        break
    
    else:
        print("Opção inválida. Tente novamente.")
