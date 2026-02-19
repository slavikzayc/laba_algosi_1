# -*- coding: utf-8 -*-
# 2
import time
# весь код почти совпадает с первым заданием, я не буду это заново коментить

start = time.perf_counter()

file = open('input1.txt')

n = file.readline()

arr = list(map(int, file.readline().split()))

count = [1] # список, в который будут вноситься нужные индексы

for i in range(1, len(arr)):
    key = arr[i] 
    j = i - 1

    while j >=0 and arr[j] > key:
        arr[j + 1] = arr[j] 
        j -= 1
    arr[j + 1] = key 
    count.append(j + 2) # ну тут совсем легко, просто после того как нашли место для ключа добавляем индекс в count. + 2 так как в задаче сказано, что нумерация начинается с 1, а не с 0

output = open('output1.txt', 'w')

for el in count:
    output.write(str(el))
    output.write(' ')

for el in arr:
    output.write(str(el))
    output.write(' ')

output.close()

end = time.perf_counter()

print(end - start)