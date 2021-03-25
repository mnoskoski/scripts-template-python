"""
Loop for

Loop -> estrutura de repeticacao
For -> uma das estruturas

for item in interavel:
    //execucao do loop

Utilizamos loop para iterar sobre sequencia ou sobre valores iteraveis()
String 
 nome = 'Marcelo'

Lista
  list =  [1,2,3,4]

Range
  numero

nome = 'Marcelo'
lista = [1, 3, 4, 5, 7]
numeros = range(1,10)

# Exemplo iterando sobre uma string
for letra in nome:
    print(letra)

# Exemplo iterando sobre uma lista
for numero in lista:
    print(numero)

# Exemplo iterando sobre range
for numero in range(1,10):
    print(numero)

"""

# nome = 'Marcelo'
# lista = [1, 3, 4, 5, 7]
# numeros = range(1,10)

# for indice, letra in enumerate(nome):
#     print(nome[indice])

# for indice, letra in enumerate(nome):
#     print(letra)

# for valor in enumerate(nome):
    # print(valor)



# qtd = int(input('Quantas vezes esse loop deve rodar?'))

# for n in range(1, qtd):
#     print(f'imprimindo {n}')



#Original: U+1F60D
#Modificado: U0001F60D
num_range=10
emoji = "U0001F60D"
for num in range(num_range):
    for num in range(1,11):
        print('\U0001F60D' * num)
        for num in range(4):
            print('\U0001F60D' * num)


fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)