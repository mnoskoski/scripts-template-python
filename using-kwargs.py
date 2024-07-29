# -*- coding: utf-8 -*-
"""
def cores_favoritas(**kwargs):
    for pessoa, cor in kwargs.items():
        print(f' A cor favorita de  { pessoa.title() }  é {cor} ')

cores_favoritas(marcelo='azul', joao='verde')


##parametro args ou kwargs nao sao obrigatorios

def cumprimento_especial(**kwargs):
    if 'geek'in kwargs and kwargs['geek'] == 'Python':
        return "voce recebeu um cumprimento pythonico Keeg"
    elif 'geek' in kwargs:
        return f"{kwargs['geek']} Geek!" 
    return "Nao tenho certeza quem é voce..."


print(cumprimento_especial())
print(cumprimento_especial(geek='Python'))
print(cumprimento_especial(geek='Oi'))
print(cumprimento_especial(geek='Especial'))


## parametros na ordem correta
def mostra_info( a, b, *args , instrutor='Geek', **kwargs) :
    return [a, b, args, instrutor, kwargs]
"""
## parametros na ordem incorreta
def mostra_info( a, b, instrutor='Geek', *args ,**kwargs) :
    return [a, b, args, instrutor, kwargs]

print(mostra_info(1, 2, 3, sobrenome='Noskoski', cargo='devops'))



def mostra_nome(**kwargs):
    return f"{kwargs['nome'] } {kwargs['sobrenome']}"

nomes = {'nome': 'Marcelo', 'sobrenome': 'Noskoski'}

print(mostra_nome(**nomes))