import random

above_zero_count = 0
s = 0
n = int(input('Рамер матрицы: '))
m = [ [ random.randrange(10) for i in range(n) ] for j in range(n)]

for i in range(n):
    for j in range(i+1, n):
        if m[i][j] > 0:
            above_zero_count += 1
            s += m[i][j]

for i in m:
    for j in i:
        print(j, end="  ")
    print()


print('Сумма: ', s)
print('Количесто положительных цифр: ', above_zero_count)