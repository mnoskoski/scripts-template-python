

countries=['br','FR','eua']

for i in range(len(countries)):
    print("Country: " + countries[i].upper())
    #countries.append(input("digit other country:"))
    #for i in range(len(countries)):
    #    print("Country: " + countries[i].lower())

ages = [10, 22, 34, 55]
for i in range(len(ages)):
    if(ages[i] >= 18 ):
        print("Pessoa de maior com idade de: ", + ages[i])
    else:
        print("Pessoa de menor com idade de: ", + ages[i])