"""
Formatação básica de strings
s - string
d - int
f - float
.<número de dígitos>f
x ou X - Hexadecimal
(Caractere)(><^)(quantidade)
> - Esquerda
< - Direita
^ - Centro
= - Força o númetro a aparecer antes dos zeros
Sinal - + ou -
Ex.: 0>-100,.1f
Conversoin flags - !r !s !a
"""
variavel = 'ABC'
print(f'{variavel}')
print(f'{variavel: >10}')
print(f'{variavel: <10}.')
print(f'{variavel: ^10}.')
print(f'{1000.457899658878996655599666558999:0>+10.1f}')
print(f'O hexadecimal de 10500 é {1500:08x}')
print(f'{variavel!r}')




