"""
Faça um programa que peça ao usuário para digitar um número inteiro, 
informe se este número é par ou ímpar. Caso o usuário não digite o número 
inteiro, informe que não é um número inteiro.
"""
numero = input('Digite um número inteiro: ')

if numero.isdigit():
    numero = int(numero)
    if numero % 2 == 0:
        print('Número par')
    else:
        print('Número ímpar')
else:
    print('Você não digitou um número inteiro')
"""
Faça um programa que pergunte a hora e, baseando-se no horário
descrito, exiba a saudação apropriada. Ex.:
Bom dia 01-11
"""
hora = input('Digite o horário atual de 0-23: ')

try:
    hora = float(hora)

    if (hora >= 0 and hora <= 11):
        print('Bom dia.')
    elif (hora >= 12 and hora <= 17):
        print('Boa tarde.')
    elif (hora >= 18 and hora <= 23):
        print('Boa noite')
    else:
        print( 'Você digitou fora do formato estabelecido.')
except:
    print('Você não digitou um número')


# Faça um programa que peça o primeiro nome. Se o nome tiver 4 letras ou 
# menos, escreva "Seu nome é curto"; se tiver entre 5 e 6 letras, escreva
# "Seu nome é normal"; maior que 6 letras "Seu nome é muito grande".

nome = input('Digite seu nome: ')

if len(nome) <= 4:
    print(f'Seu nome é curto, tem {len(nome)} letras')
elif len(nome) >= 5 and len(nome) <= 6:
    print(f'Seu nome é normal, tem {len(nome)} letras')
else:
    print(f'Seu nome é grande, tem {len(nome)} letras')