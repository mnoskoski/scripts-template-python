def mean_func(list1):
    return sum(list1) / len(list1) #len retorna o numero de objetos dentro de uma lista

print(mean_func([5, 6,7, 8]))

#### using argv

def using_argv(*args):
    print(args)

using_argv('Hello', 'World')

#
test = '20'

if test == 'true':
    print(1)
elif test == 'false':
    print(2)
else:
    print(test)

def my_function(*argv):
  print(argv[0])

my_function('Hello', 'World!')

def sum(*args):
    result=0
    for arg in args:
        result += arg
        print("show arg: ", arg)
    return result 
print(sum(6,3,1))


def sum2(a,b):
    return a+b
print(sum2(2,3))

def functionAges(*ages):
  print("The older friend is " + ages[0] + " years")

functionAges("13", "12", "11")


def showArguments(*argv):  
    for arg in argv:  
        print('argumento: ',  arg ) 

showArguments('Hello', 'World!')