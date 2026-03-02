# 2
import time


start = time.perf_counter()

file = open('input2.txt')

n = file.readline()

arr = list(map(int, file.readline().split()))

count = [1] # массив, в котором будут храниться индексы после перестановок

for i in range(1, len(arr)): # алгоритм как в задании 1
    key = arr[i] 
    j = i - 1

    while j >= 0 and arr[j] > key:
        arr[j + 1] = arr[j] 
        j -= 1
    arr[j + 1] = key 
    count.append(j + 2) # добавляем индекс после перестановки в массив. +2 т.к. счёт индексов начинается с 1.

output = open('output1.txt', 'w')

for el in count:
    output.write(str(el))
    output.write(' ')

print('', file = output)

for el in arr:
    output.write(str(el))
    output.write(' ')

output.close()

end = time.perf_counter()

print(end - start)