import time


def selection_sort(arr, n):
    for i in range(n):
        key = i # берем первый, в неотсортированной части массива, элемент как минимальный
        for j in range(i + 1, n):
            if arr[j] < arr[key]: # ищем для него место в отсортированной части
                key = j

        arr[i], arr[key] = arr[key], arr[i] # тут происходит swap
    return arr


start_time = time.perf_counter()

file = open('input.txt')

n = int(file.readline())

arr = [int(l) for l in file.readline().split()]

file.close()

arr = selection_sort(arr, n)

output = open('output.txt', 'w')

for el in arr:
    output.write(str(el))
    output.write(' ')

output.close()

end_time = time.perf_counter()

print(end_time - start_time)
