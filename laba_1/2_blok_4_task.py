# 4
import time
start = time.perf_counter()


file = open('input4.txt')

arr = [int(l) for l in file.readline().split()]

V = int(file.readline())


def lin_search(arr, V):
    count = []
    for i in range(len(arr)):
        if V == arr[i]:
            count.append(i)
    return count


c = lin_search(arr, V)

output = open('output.txt', 'w')

if len(c) == 0:
    output.write('-1')
elif len(c) == 1:
    output.write(str(c[0]))
else:
    output.write(str(len(c)))
    for el in c:
        output.write(str(el))

output.close()

end = time.perf_counter()

print(end - start)