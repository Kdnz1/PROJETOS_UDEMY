"""
    Faça um jogo para o usuário adivinhar qual a palavra secreta.
    - Você vai propor uma palavra secreta qualquer e vai dar a possibilidade para o usuário digitar apenas uma letra. - Quando o usuário digitar uma letra você  vai conferir se a letra digitada está na palavra secreta.

        - Se a letra digitada estiver na palavra secreta; exiba a letra;
        - Se a letra digitada não estiver na palavra secreta; exiba *.
    Faça a contagem de tentativas do seu usuário.
"""

palavra_secreta = 'queijo'
palavra_mostrada = '_' * len(palavra_secreta)
tentativas = 0
erros = 6
letras = ''

print("Bem-vindo ao jogo da forca!")
print(f"A palavra tem {len(palavra_secreta)} letras.\n{palavra_mostrada.center(30)}")


while True:
    palavra_formada = ''
    solicita_letra = input('Digite uma letra: ')

    if solicita_letra in ' ':
        print('Preencha com uma letra')
        continue
    elif solicita_letra.isdigit():
        print('Números são proibidos.')
        continue
    elif len(solicita_letra) > 1:
        print('Somente um letra é permitida.')
        continue
    elif solicita_letra in letras:
        print('Você já tentou essa letra.')
        continue
    elif solicita_letra in palavra_secreta:
        letras += solicita_letra

    tentativas += 1

    if solicita_letra not in palavra_secreta:
        erros -= 1
        print('Essa letra não se encontra na palavra.')
        print(f'Se você errar mais {erros} vezes, perde o jogo.')
        print('')
        if erros == 0:
            print('Você perdeu!')
            break

    for letra_secreta in palavra_secreta:
        if letra_secreta in letras:
            palavra_formada += letra_secreta
        else:
            palavra_formada += '_'

    print('Palavra formada:', palavra_formada)

    if palavra_formada == palavra_secreta:
        print('')
        print('')
        print('VOCÊ GANHOU!! PARABÉNS!')
        print(f'A palavra era {palavra_secreta.upper()}.')
        print('Tentativas:', tentativas)
        print("Obrigado por jogar.")
        break
