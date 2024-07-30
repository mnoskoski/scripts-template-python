matrix = [[j for j in range(3)] for i in range(3)] 
print(matrix)

##
a = []
for i in range(5):
    a.append([])
    for j in range(5):
        a[i].append(j)

print(a)

nome="joao"
for indice, letra in enumerate(nome):
    print(indice, ": "+letra)

for i in range(len(nome)):
    print((nome[i]))
