import time

# 1

start = time.perf_counter()

file = open('input.txt')

n = int(file.readline())

arr = list(map(int, file.readline().split()))

file.close()

for i in range(1, n):  # начинаем перебор со второго элемента
    key = arr[i]  # первый элемент из неотсортированной части массива
    j = i - 1

    while j >= 0 and arr[j] > key:  # поиск подходящего места для key
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
