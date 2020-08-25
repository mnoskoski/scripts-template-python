#/usr/bin/python
#teste da funcao 'len' para pegar a quantidade de caracter de uma string

import sys
import requests
s = len(sys.argv[1])

def right_justify(s):
    print('tamanho da string:', +s )
    
if __name__ == "__main__":
 right_justify(s)