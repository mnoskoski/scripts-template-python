#/usr/bin/python
#usando and 'trunegacao no python
#False and True deve ser escrito em maiusculo 

ativo = True
print(ativo)
logado = True

def validacaUsuarioConectado():
    if logado == False:
        print ("usuario desconectado")
    else:
        print("usuario conectado")

if __name__ == "__main__":
    validacaUsuarioConectado()