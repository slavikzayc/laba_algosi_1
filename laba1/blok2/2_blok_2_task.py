# 2
import time

file = open('input2.txt')

n = int(file.readline())

arr = list(map(int, file.readline().split()))

count = [1] # массив, в котором будут храниться индексы, на которые были переставлены элементы исходного массива

start = time.perf_counter()

file.close()

for i in range(1, n):
    key = arr[i]
    j = i - 1

    while j >= 0 and arr[j] > key:
        arr[j + 1] = arr[j]
        j -= 1
    arr[j + 1] = key
    count.append(j + 2) # j + 2 так как индексы должны начинаться с 1

output = open('output.txt', 'w')

for el in count:
    output.write(str(el))
    output.write(' ')

print('', file=output)

for el in arr:
    output.write(str(el))
    output.write(' ')

output.close()

end = time.perf_counter()

print(end - start)
