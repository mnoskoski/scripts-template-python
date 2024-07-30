# using list in python and upper case
countries = ['br', 'ar', 'eua']

for i in range(len(countries)):
    print("Pais: " + (countries[i].upper()))

#list1=[2,5,3,1]
#print(list1[::-1])

numbers = [1, 2, 3, 4, 5]
numbers[4] = 6
print(numbers[4])



num = [4, 4, 3, 1]
num.sort()
print(num)


#list1=["Go","Java","Java","Java","Rust"]
#print(min(list1))

list1=['UK','India','Canada']
list1.insert(2,9)
print(list1)

#pop - remove specifics elements and return
list1 = [4, 4, 3, 1, 5, 6, 7]
list1.pop(1)
print(list1)

for x in [0, 1, 1, 3]:
    for y in [0, 2, 1, 2]:
        print("*" * 20)



list1 = [1, 2, 3, 4]
for index, j in enumerate(list1):
     print(index, j)


list1 = [[1,2,3,2,5],[1,2,3,4],[4,5,6,7],[8,9,10,7]]
for i in list1:
    if len(i)==4:
      print(i)


list1 = [1, 2, 3, 4]
for index, j in enumerate(list1):
     print(index, j)

letters = ["A", "B", "C", "D", "E"]
print(letters[1:])