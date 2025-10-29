"""
Calculo do primeiro dígito do CPF
CPF: 746.824.890-70
Colete a soma dos 9 primeiros dígitos do CPF
multiplicando cada um dos valores por uma
contagem regressiva começando de 10

Ex.:  746.824.890-70 (746824890)
   10  9  8  7  6  5  4  3  2
*  7   4  6  8  2  4  8  9  0
   70  36 48 56 12 20 32 27 0

Somar todos os resultados: 
70+36+48+56+12+20+32+27+0 = 301
Multiplicar o resultado anterior por 10
301 * 10 = 3010
Obter o resto da divisão da conta anterior por 11
3010 % 11 = 7
Se o resultado anterior for maior que 9:
    resultado é 0
contrário disso:
    resultado é o valor da conta

O primeiro dígito do CPF é 7
"""
lista_cpf_invalidos = [
    '00000000000',
    '11111111111',
    '22222222222',
    '33333333333',
    '44444444444',
    '55555555555',
    '66666666666',
    '77777777777',
    '88888888888',
    '99999999999'
    ]

while True:
    cpf = input('Digite seu cpf, irei fazer a validação: ')

# Remove ponto ou traço se caso o usuário colocar
    cpf_numeros = cpf.replace(".", "").replace("-", "")
    try:
        if len(cpf_numeros) > 11:
            print('Um CPF possue somente 11 números.\nInsira novamente.')
        elif cpf_numeros in lista_cpf_invalidos:
            print('Esse CPF não é permitido fazer a validação.')
        else:
            PRIMEIROS_NOVE_NUMEROS = cpf_numeros[:9]
            CONTADOR_REGRESSIVO_1 = 10
            resultado_primeiro_digito = 0
            for digito in PRIMEIROS_NOVE_NUMEROS:
                resultado_primeiro_digito += int(digito) * CONTADOR_REGRESSIVO_1
                CONTADOR_REGRESSIVO_1 -= 1
            primeiro_digito = (resultado_primeiro_digito * 10) % 11
            primeiro_digito = primeiro_digito if primeiro_digito <= 9 else 0



            PRIMEIROS_DEZ_NUMEROS = cpf_numeros[:10]
            CONTADOR_REGRESSIVO_2 = 11
            resultado_segundo_digito = 0
            for digito in PRIMEIROS_DEZ_NUMEROS:
                resultado_segundo_digito += int(digito) * CONTADOR_REGRESSIVO_2
                CONTADOR_REGRESSIVO_2 -= 1
            segundo_digito = (resultado_segundo_digito * 10) % 11
            segundo_digito = segundo_digito if segundo_digito <= 9 else 0


            cpf_calculo = f'{PRIMEIROS_NOVE_NUMEROS}{primeiro_digito}{segundo_digito}'
            if cpf_numeros == cpf_calculo:
                print(f'{cpf_numeros[0:3]}.{cpf_numeros[3:6]}.{cpf_numeros[6:9]}-{cpf_numeros[9:]} - CPF VÁLIDO.')
            else:
                print(f'{cpf_numeros[0:3]}.{cpf_numeros[3:6]}.{cpf_numeros[6:9]}-{cpf_numeros[9:]} - CPF INVÁLIDO.')
    except ValueError:
        print('Somente números são permitidos.')