"""
    Faça uma lista de compras com listas
    O usuário deve ter a possibilidade de inserir, apagar e listar valores da sua lista, não permita que o programa quebre com erros de indices inexistentes na lista.
"""

lista_compras = []
LINHA = '-' * 25
CONTADOR = 1

while True:
    print('''
    O que você pretende realizar?
    1 - Inserir Item
    2 - Apagar Item
    3 - Listar Itens
    4 - Sair''')
    print(LINHA)
    solicita_opcao = input('Digite a opção desejada: ')

    if solicita_opcao == "1":
        adicionar_item = input('O que você deseja inserir? ')
        if adicionar_item.isdigit():
            print('Números não são permitidos.')
            print(LINHA)
            continue
        elif not adicionar_item:
            print('Preencha com algo.')
        elif adicionar_item in lista_compras:
            print('Este item já foi adicionado.')
            print(LINHA)
            continue
        else:
            lista_compras.append(adicionar_item)
            print(f'O item {adicionar_item} foi adicionado a lista com sucesso!')
            print(LINHA)

        while True:
            mais_itens = input('Deseja adicionar mais algum item? [S]im [N]ão: ').upper()
            if mais_itens == 'S':
                adicionar_item = input('O que você deseja inserir? ')
                print(LINHA)
                if not adicionar_item:
                    print('Preencha com algo.')
                elif adicionar_item in lista_compras:
                    print('Este item já foi adicionado.')
                    print(LINHA)
                    continue
                else:
                    lista_compras.append(adicionar_item)
                    print(f'O item {adicionar_item} foi adicionado a lista com sucesso!')
                    print(LINHA)
            elif mais_itens == 'N':
                print(LINHA)
                break
            else:
                print('Opção inválida.')


    elif solicita_opcao == "2":
        if not lista_compras:
            print('Não tem nenhum item na lista, adicione algo.')
            print(LINHA)
            continue
        for indice, item in enumerate(lista_compras):
            indice += CONTADOR
            print(indice,'-',item)
        print(LINHA)
        apagar_item = input('O que você deseja apagar?\n(Coloque o número do item):')
        try:
            if apagar_item.isdigit():
                lista_compras.pop(int(apagar_item))
                print(f'O item {apagar_item} da lista foi deletado.')
                print(LINHA)
            else:
                print('Somente o número é permitido.')
                print(LINHA)
        except IndexError:
            if apagar_item not in lista_compras:
                print('Item não se encontra na lista.')


    elif solicita_opcao == "3":
        if not lista_compras:
            print('Não tem nenhum item na lista, adicione algo.')
            print(LINHA)
            continue
        print('Lista de compras:')
        for indice, item in enumerate(lista_compras):
            indice += CONTADOR
            print(indice,'-',item)
        print(LINHA)

    elif solicita_opcao == "4":
        print('Até a próxima!')
        break
    else:
        print('Opção inválida.')
        continue