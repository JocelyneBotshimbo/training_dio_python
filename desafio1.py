# Sistema Bancário em Python

operacao ="""
[d]Depositar
[s]Sacar
[e]Extrato
[q]Sair
"""

saldo = 0
limite = 500
extrato = ''
numero_saque = 0
limite_saque = 3

while True:
    opcao = input(operacao)
     
    if opcao == 'd':
        deposito = float(input('Informe o valor do depósito: '))
        
        if deposito > 0:
            saldo = saldo + deposito
            extrato = extrato + f"Depósito: R$ {saldo:.2f}\n"
        else:    
            print('Não aceitamos o valor negativo')

    elif opcao == 's':
        saque = float(input('Informe o valor do saque: '))
        
        excedeu_saldo = saque > saldo
        excedeu_limite = saque > limite
        excedeu_saques = numero_saque >= limite_saque

        if excedeu_saldo:
            print("Saldo não suficiente")
        elif excedeu_limite:
            print("Saque excedeu o limite")
        elif excedeu_saques:
            print("Número de saque excedeu")

        elif saque > 0:
            saldo = saldo - saque
            extrato = f"Saque: R$ {saque:.2f}\n" 
            numero_saque = numero_saque + 1

        else:
            print("Valor informado é inválido")    
            
    elif opcao == 'e': 
        print("\n##########Extrato##########")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("##############################")   
    
    elif opcao == 'q':
        break 
    else:
        print('Operação inválida! Por favor informar a opção correta desejada')   