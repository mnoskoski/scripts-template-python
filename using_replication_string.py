
numer = input("Digite um numero: ")

#using replication operation string
for i in numer:
    print("+" + i * "-" + "+")
    print(("|" + " " * 10 + "|\n") * 5, end="")
    print("+" + i * "-" + "+")
