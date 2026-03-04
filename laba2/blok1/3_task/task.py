def h_index(arr):
    arr.sort(reverse=True)
    h = 0
    for i in range(len(arr)):
        if arr[i] >= i + 1:
            h = i + 1
        else:

            break
    return h


file = open('input.txt')

arr = list(map(int, file.readline().split()))

file.close()


output = open('output.txt', 'w')

output.write(str(h_index(arr)))


