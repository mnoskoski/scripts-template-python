"""
Escopo de variaveis
Dois casos
1- Globais
   - sao reconhecidas, ou seja, o escopo é todo o programa
2- Locais
   - sao reconhecidas apenas no bloco onde foram declaradas

Para declarar variaveis:
nome_variavel = valor_variavel

"""

numero = 10
print(numero)
print(type(numero))

numero = "10"
print(numero)
print(type(numero))
#novo =0

numero = 11
if numero > 10:
    novo = numero +5
    print(novo)

#print(novo)