import random

N = int(input('Кол-во строк: '))
M = int(input('Кол-во столбцов: '))

MN = [ [ random.randrange(10) for i in range(M) ] for j in range(N)]
print('Изначальная матрица: ')
for i in MN:
    for j in i:
        print(j, end="  ")
    print()

for i, row in enumerate(MN):
    max = 0
    min = 0
    for j, elem in enumerate(row):
        if elem > row[max]:
            max = j
        if elem < row[min]:
            min = j
    first_temp = row[0]
    row[0] = row[max]
    row[max] = first_temp
    last_temp = row[-1]
    row[-1] = row[min]
    row[min] = last_temp

print('После применения условий: ')
for i in  MN:
    for j in i:
        print(j, end="  ")
    print()