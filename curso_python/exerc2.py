#exerc python (if, while - pares e impares)

import sys 

varA = sys.argv[1]
x = 1

while x <= int(varA):
    if int(x) % 2 == 0:
        print ("Execucao" + str(x) + ": " + str(x) + " é par")
        x = x+1 
    else:
        print("Execucao" + str(x) + ": " + str(x) + " é impar")
        x = x+1 
    
