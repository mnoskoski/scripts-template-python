test = ("Marcelo", 30)

nome, idade = test
print(f"Nome: {nome}, Idade: {idade}")


#para desustrutrar o dicionar eu posso usar o _ para tirar um ValueError
#posso usar oo ** 

people = (
    {
        "name" : "Mateus",
        "age" : 28
    },
    {
        "name" : "Joao",
        "age" : 29
    },
    {
        "name" : "Teste",
        "age" : 29
    },
    {
        "name" : "Gabriel",
        "age" : 29
    },
)

# unpack a tuple of dicts
for person in people:
    name, age = person.values()
    print(f"{name} is {age} years old")
 
# ignore specific field with _
for person in people:
    name, _ = person.values()
    print(f"His name is {name}")
 
# unpack with * (list)
first, *middle, last = people
print(middle)
 
def print_people_info(name, age):
    print(f"{name} is {age} years old")
 
# unpack with ** (dict)
for person in people:
    print_people_info(**person)
 

