
# TASK 2.1
s = 0
n = int(input("Введите целое число n: "))
for i in range(1, n + 1):
    t = i * ( i + 1 )
    s += (1.0 / t)

print("Cумма ряда: ",  s)



# TASK 2.2
import math

sum = 0
i = 1
e = math.e
E = float(input('\nТочность эпсилона: '))
series = math.sqrt(i + 1) / (i * e)
while (series >= E):
    e *= math.e
    sum += series
    i += 1
    series = math.sqrt(i + 1) / (i * e)
print('Сумма ряда: ', sum)