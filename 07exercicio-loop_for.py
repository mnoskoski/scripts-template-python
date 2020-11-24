""" 
Loop -> estrutura de repeticao
for é uma dessas estrutura 

C ou Java

for (i=0; i <10; i++){
    //instrucao
}

Python

for item in interavel:
    //execucao do loop


Utilizamos loops para criar lacos de repeticao

Exemplo de iteraveis:
  - string
      nome = 'geek univesity'
  - Lista:
      list = [11, 12]
  - Range
      numero = range[1, 10]
""" 
nome = 'Geek University'
lista = [1, 3, 5, 7, 9]
numeros = range(1, 10)  #deve ser transformado em uma lista

#exemplo de for 1 
for letra in nome:
    print(letra)

#exemplo de for 2
for numero in lista:
    print(numero)

#exemplo de for 3
for numero in range(1, 10):
    print(numero) 