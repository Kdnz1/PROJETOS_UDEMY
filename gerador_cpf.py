"""
    GERADOR DE CPF
"""
import random

nove_numeros = ''
for i in range(9):
    nove_numeros += str(random.randint(0,9))
CONTADOR_REGRESSIVO_1 = 10
resultado_primeiro_digito = 0
for digito in nove_numeros:
    resultado_primeiro_digito += int(digito) * CONTADOR_REGRESSIVO_1
    CONTADOR_REGRESSIVO_1 -= 1
primeiro_digito = (resultado_primeiro_digito * 10) % 11
primeiro_digito = primeiro_digito if primeiro_digito <= 9 else 0


PRIMEIROS_DEZ_NUMEROS = nove_numeros + str(primeiro_digito)
CONTADOR_REGRESSIVO_2 = 11
resultado_segundo_digito = 0
for digito in PRIMEIROS_DEZ_NUMEROS:
    resultado_segundo_digito += int(digito) * CONTADOR_REGRESSIVO_2
    CONTADOR_REGRESSIVO_2 -= 1
segundo_digito = (resultado_segundo_digito * 10) % 11
segundo_digito = segundo_digito if segundo_digito <= 9 else 0


cpf_calculo = f'{nove_numeros}{primeiro_digito}{segundo_digito}'


print(f'Aqui está seu novo CPF: {cpf_calculo[0:3]}.{cpf_calculo[3:6]}.{cpf_calculo[6:9]}-{cpf_calculo[9:]}')
