# Operadores lógicos
# and (e) or (ou) not (não)
# and - Todas as condições precisam ser verdadeiras.
# Se qualquer valor for considerado falso, 
# a expressão inteira será avaliada naquele valor 
# São considerados falsy (que você já viu): 0 0.0 '' False
# Também existe o tipo None que é 
# usado para representar um não valor


# entrada = input('[E]ntrar [S]air: ')
# senha_digitada = input('Senha: ')

# senha_permitida = '123456'

# if (entrada == 'E' or entrada == 'e') and senha_digitada == senha_permitida:
#     print('Entrar')
# else:
#     print('Sair')

# Avaliação de curto circuito
# print(True and False and True)
# print(bool (0.0))
# print(True and 0 and True)

print(0 or False or 'abc' or True)