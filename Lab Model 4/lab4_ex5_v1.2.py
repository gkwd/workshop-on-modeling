arr_1 = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14]
arr_2 = [15,16,17,18,19,20,21,22,23,24,25,26,27,28,29]
arr_3 = [30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45]

def arr_sum(arr):
    sum_of_arr = 0
    i = 0
    while i < len(arr):
        sum_of_arr += arr[i]
        i += 1
    return sum_of_arr


def average(arr):
    av = 0.0
    i = 0
    while i < len(arr):
        av += arr[i]
        i += 1
    av /= (len(arr) +1) 
    return av


print("Сумма элементов первого массива: ", arr_sum(arr_1))
print("Среднее арифметическое значение первого массива:", average(arr_1))
print("Сумма элементов второго массива:", arr_sum(arr_2))
print("Среднее арифметическое значение второго массива:", average(arr_2))
print("Сумма элементов третьего массива:", arr_sum(arr_3))
print("Среднее арифметическое значение третьего массива:", average(arr_3))