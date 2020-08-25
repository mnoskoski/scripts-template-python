"""
Estruturas logiscas

and (e)
or (ou)
not (nao)


operadores unarios
  - not

operadores binarios
  - and, or, is

Para o and ambos valores precisam ser True
Para o or um ou outro valor precisa ser True
Para o not o valor do booleano é invertido, se for True vira false e for false vira True
Para o is o valor é comparado com o segundo valor
"""

ativo = True
logado = False
if ativo and logado:
    print('Bem vindo usuario!')
else:
    print('Voces precisa ativar sua conta!')

#Ativo é verdadeiro?
print(ativo is True)

