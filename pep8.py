"""
Comentarios no python 3 aspas duplas coemcandos 3  o final "


PEP8 - Python Enhancement proposal

São propostas de melhorias para a linguagem Python 

The Zen of Python

import this

A ideia da PEP8 é que possamos escrever codigos Python de forma Pythonica

[1] Utilize Camel Case para nomes de classes;

class Calculadora:
    pass


class CalculadoraCientifica:
    pass


[2] Utilize nomes em minusculos, separados por underline para funcoes e variaves;

def soma():
    pass


def soma_dois():
    pass

numero = 4

[3] Utilize 4 espacoes para identacao

if 'a' in 'banana':
    print('tem')

[4] Linhas em branco
  - separar funcoes e definicoes com duas linhas em branco
  - metodos dentro de uma classe devem ser separados com uma unica linha em branco

[5] Imports
  - Imports devem ser seprados feitos em linhas separadas 

class Classe:
    pass

class Outra:
    pass



# Import Errado 

import sys, os

#Import Certo

import sys
import os

# Nao tem problemas em utilizar:

from types import StringType, ListType

#Caso tenha muitos imports de um mesmo pacote, recomenda se fazer:

from types import(
    StringType,
    ListType,
    SetType,
    OutroType
)

# imports devem ser colocados no topo do arquivo,  logo depois de qualquer 
# comentario ou docstrings e antes de constantes ou variaveis globais
# imports vao na primeira linha

  #
  

[6] Espacos em expressoes e instrucoes 

Nao faca:

funcao_algo( algo[ 1 ], { outro: 2 } )

faca:
funcao(algo[1], {outro: 2})

nao faca:
algo (1)

faca:
 algo(1)

nao faca:
dict ['chave'] = lista [indice]

faca:
dict['chave'] = lista[indice]


nao fazer:
x              = 1
y              = 2
variavel_longa = 4

Python=  

  - string em python
  - dir e help
  - funcao
  - classes 


"""


from random import randrange, uniform
print(randrange(1, 60))
