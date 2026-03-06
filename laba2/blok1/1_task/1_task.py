def anti_qsort(n):
    file = open('output.txt', 'w')

    if n == 1:
        file.write('1')
        return

    arr = [1, 2]

    for i in range(2, n):
        arr.append(i + 1)

        arr[i // 2], arr[i] = arr[i], arr[i // 2]

    for el in arr:
        file.write(str(el))
        file.write(' ')
    file.close()


file = open('input.txt')

n = int(file.readline())

anti_qsort(n)