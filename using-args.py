
def soma_todos_numeros(*args):
    return sum(args)

##criando um array para ser passado
numeros = [1, 2, 3, 4, 5, 6, 7]

##o * informa que passamos uma colecao de dados como argumento, ele desempacta e usa os dados
print(soma_todos_numeros(*numeros))

