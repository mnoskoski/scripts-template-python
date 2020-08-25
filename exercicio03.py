"""
Tipo String

EM python, um dado é considerado do tipo string sempre que:

- Estive entre aspas, simples ou duplas -> "a" , 'a'
- Estiver entre aspas simples triplas -> '''a'''

nome = 'Marcelo Noskoski'
print(nome)
print(type(nome))

nome = "Marcelu's"
print(nome)
print(type(nome))

nome = 'Angelina \nJolie'
print(nome)
print(type(nome))

nome = "Marcelo"
print(nome.upper())
print(type(nome))

nome = "Marcelo"
print(nome.lower())
print(type(nome))

## transforma em uma lista de string 
nome = '''Marcelo'''
print(nome.split())
print(nome[0:4]) #Slice de string

#transformo em uma lista de strings separados pelo espaco
nome = 'Marcelo oi'
print(nome.split()[1])

# Uso pra escrever a string ao contrario - inversao da string
nome = 'Marcelo'
print(nome[::-1])

# Substituo a letra M por L
nome = 'Marcelo'
print(nome.replace('M' , 'L'))

# Substituo a letra M por L
texto = 'socorram me subino onibus em marrocos' #palindromo
print(texto)
print(texto[::-1])

"""


