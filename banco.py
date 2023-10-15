menu = """ 
    [1] Depositar
    [2] Sacar
    [3] Extrato
    [0] Sair
=> """

saldo = 0
numero_saques = 0
extrato = ''
LIMITE_SAQUES = 3
LIMITE_VALOR = 500 

while True :
    opcao = input(menu)

    if opcao == '1' :
        valor_deposito = float(input("Digite o valor do depósito: "))

        if valor_deposito <= 0:
             print("Operação inválida! O valor do depósito deve ser maior que zero.")
        else:     
            saldo += valor_deposito
            extrato += f"Depósito: R$ {valor_deposito:.2f}\n"
            print(f"Depósito no valor de R$ {valor_deposito:.2f} realizado com sucesso!")

    elif opcao == '2' :    
        valor_saque = float(input('Digite o valor do saque: '))
        excedeu_saldo = valor_saque > saldo
        excedeu_saque = numero_saques >= LIMITE_SAQUES
        excedeu_limite = valor_saque > LIMITE_VALOR

        if excedeu_saldo :
            print("Saldo insuficiente!")

        elif excedeu_saque : 
            print("Voce atingiu o limite da quantidade de saques diários!")

        elif excedeu_limite :
            print("Limite de R$ 500.00 para saques excedido!")

        elif valor_saque > 0 :
            saldo -= valor_saque
            numero_saques += 1
            extrato += f"Saque: R$ {valor_saque:.2f}\n"
            print(f"Saque no valor de R$ {valor_saque:.2f} realizado com sucesso!")

        else :
            print("Valor inválido!")

    elif opcao == '3' : 
        print("\n__________EXTRATO__________")
        print("Nenhuma movimentação realizada" if not extrato else extrato)
        print(f'\nSALDO: R$ {saldo:.2f}')
        print("_____________________________")

 

    elif opcao == '0' :
        break

    else : 
        print('Opção inválida! Por favor, selecione a opção desejada.')
   

