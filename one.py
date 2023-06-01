while True:
    print('{:=^40}'.format(' ESTUDOS ENEM '))
    print('MATÉRIAS  [ 1 ]')
    print('SOBRE     [ 2 ]')
    print('SAIR      [ 3 ]')
    escolha_init = int(input('Sua escolha: '))
    if escolha_init == 1:
        print('ok')
    elif escolha_init == 2:
        print('ok')
    elif escolha_init == 3:
        break
    else:
        print('{:-^40}'.format(' ERROR '))
        print('Opção inválida. Tente novamente...')
        print('{:-^40}'.format(' ERROR '))