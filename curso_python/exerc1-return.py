## Marcelo Noskoski
## Objetivo: treinar funcoes com retorno tratando otipo de dado do retorno

import sys

def func_return( num1 , num2):
    sum = num1 + num2 
    return sum

v1 = sys.argv[1]
v2 = sys.argv[2]

print("o valor é:  "+  str(func_return(int(v1), int(v2))))

####
def return_greeting():
  return "Olá mundo!"
print(return_greeting())

##
def is_true(a): 
  return bool(a) 
result = is_true(int(v1)<int(v2)) 
if result == True:
    print("O resultado é", result, str(v1) + " é menor que " + str(v2))
else:
    print("O resultado é", result, str(v2) + " é menor que " + str(v1))

###

def my_function(x):
  return 10 / x

print(my_function(2))