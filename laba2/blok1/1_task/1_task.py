def anti_qsort(n):
    file = open('output.txt', 'w')

    if n == 1: # если n = 1, то возможна единственная перестановка
        file.write('1')
        return

    arr = list(range(1, n + 1))

    for i in range(2, n): # меняем последний элемент каждого подмассива с элементом посередине этого же подмассива
        arr[i // 2], arr[i] = arr[i], arr[i // 2]

    for el in arr:
        file.write(str(el))
        file.write(' ')
    file.close()


file = open('input.txt')

n = int(file.readline())

anti_qsort(n)