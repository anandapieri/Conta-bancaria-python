from conta_bancaria import ContaBancaria

conta_ananda = ContaBancaria('Ananda', 1000.50)

while True:
    print('\nEscolha uma opção:')
    print('1. Depositar valor')
    print('2. Sacar valor')
    print('3. Exibir saldo')
    print('4. Exibir histórico de transações')
    print('5. Sair')

    opcao = input('Digite o número da sua opção: ')

    if opcao == '1':
        valor = float(input('Digite o valor que deseja depositar na conta: '))

        if conta_ananda.depositar(valor):
            saldo_atual = conta_ananda.exibir_saldo() #if True
            print(f'O valor R${valor:.2f} foi depositado em conta!\n{saldo_atual}')
        else:
            print('Erro no depósito! Informe um valor válido!')

    elif opcao == '2':
        valor = float(input('Digite o valor que deseja sacar da conta: '))

        if conta_ananda.sacar(valor):
            saldo_atual = conta_ananda.exibir_saldo()
            print(f'O saque no valor de R${valor:.2f} foi efetuado com sucesso!\n{saldo_atual}')
        else:
            print(f'Erro! Valor inválido ou saldo insuficiente para realizar a operação.')

    elif opcao == '3':
        print(conta_ananda.exibir_saldo())
    
    elif opcao == '4':
        print()
        print('***Histórico de Transações***')

        saldo_atual = conta_ananda.exibir_saldo()
        if not conta_ananda.exibir_extrato():
            print(f'Histórico de transações não encontrado!\n{saldo_atual}')
        else:
            for transacao in conta_ananda.exibir_extrato():
                print(transacao)
            print(saldo_atual)
    
    elif opcao == '5':
        break

    else:
        print('Opção inválida! Tente novamente')