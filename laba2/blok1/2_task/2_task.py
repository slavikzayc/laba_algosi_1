# вся идея алгоритма: разбить массив на группы из эл-ов с разницей k по индексам, отсортировать эти группы, соединить все группы и посмотреть отсортирован ли массив, если не отсортирован - задача не решаема.
def pugalo_sort(arr, n, k):
    if k >= n: # шаг больше чем размер массива, надежда только на то, что массив сразу отсортирован
        return all(arr[i] <= arr[i + 1] for i in range(n - 1))

    for sep in range(k):

        group = []
        indices = []
        i = sep

        while i < n: # создаём "группы" из элементов с разницей k индексов
            group.append(arr[i])
            indices.append(i)
            i += k

        group.sort()

        for i, val in zip(indices, group): # меняем определённые эл-ты между собой так, чтобы они были отсортированы
            arr[i] = val

    return all(arr[i] <= arr[i + 1] for i in range(n - 1)) # проверяем отсортирован ли получившийся массив

file = open('input.txt')

n, k = list(map(int, file.readline().split()))

arr = list(map(int, file.readline().split()))

file.close()

output = open('output.txt', 'w')

if pugalo_sort(arr, n, k):
    output.write("YES")
else:
    output.write("NO")
