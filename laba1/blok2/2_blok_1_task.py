import time

# 1

file = open('input.txt')

n = int(file.readline())

arr = list(map(int, file.readline().split()))

file.close()

start = time.perf_counter()

for i in range(1, n):
    key = arr[i] # первый элемент из неотсортированной части массива
    j = i - 1 # индекс последнего элемента из отсортированной части массива

    while j >= 0 and arr[j] > key:
        arr[j + 1] = arr[j]
        j -= 1
    arr[j + 1] = key

output = open('output.txt', 'w')

for el in arr:
    output.write(str(el))
    output.write(' ')

output.close()
end = time.perf_counter()

print(end - start)
