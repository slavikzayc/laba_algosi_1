def h_index(arr):
    arr.sort(reverse=True) # сортируем массив в обратном порядке
    h = 0
    for i in range(len(arr)):
        if arr[i] >= i + 1: # ищем h-index
            h = i + 1
        else:
            break
    return h


file = open('input.txt')

arr = list(map(int, file.readline().split()))

file.close()


output = open('output.txt', 'w')

output.write(str(h_index(arr)))


