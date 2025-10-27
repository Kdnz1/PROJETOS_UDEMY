''' Calculadora com while '''

while True:
    try:
        numero1 = input('Digite um número:')
        numero2 = input('Digite outro número:')
        operador = input('Qual operação desejas realizar?\n(+ ,- , * ou /):')
        
        numero1 = float(numero1)
        numero2 = float(numero2)

        linha = '-' * 30
        
        if operador == '+':
            soma = numero1 + numero2
            print('Você selecionou a operação de soma, o resultado estará abaixo:')
            print(linha)
            print(f'{numero1} + {numero2} = {soma}')
        elif operador == '-':
            subtracao = numero1 - numero2
            print('Você selecionou a operação de subtração, o resultado estará abaixo:')
            print(linha)
            print(f'{numero1} - {numero2} = {subtracao}')
        elif operador == '*':
            multiplicacao = numero1 * numero2
            print('Você selecionou a operação de multiplicação, o resultado estará abaixo:')
            print(linha)
            print(f'{numero1} * {numero2} = {multiplicacao}')
        elif operador == '/':
            divisao = numero1 / numero2
            print('Você selecionou a operação de divisão, o resultado estará abaixo:')
            print(linha)
            print(f'{numero1} / {numero2} = {divisao}')
        else:
            print('O operador selecionado está incorreto, insira uma das 4 opcões.')
            print(linha)
            continue
    except:
        print('Letras não são permitidas.')
        continue
    print(linha)
    sair = input('Desejas continuar?\n[S]im [N]ão:').lower()
    if sair == "s":
        print(linha)       
        continue
    else:
        print('Obrigado por utilizar a calculadora!\nAté a próxima.')
        break

        

    
