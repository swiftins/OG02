spisok = [1, 2, 3, 4, 5 ]

s = 0
for i in range (len(spisok)):
    s = s + spisok[i]**3
print(s)


numbers = [1, 2, 3, 4, 5]
sum_of_cubes = sum(x**3 for x in numbers)
print("Сумма кубов элементов списка:", sum_of_cubes)



