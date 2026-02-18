# -*- coding: utf-8 -*-
# 3
import time
start = time.perf_counter()

file = open('input1.txt')

n = file.readline()

arr = list(map(int, file.readline().split()))

for i in range(1, len(arr)):
    key = arr[i] 
    j = i - 1

    while j >=0 and arr[j] < key: # åäèíñòâåííîå èçìåíåíèå ïî ñğàâíåíèş ñ ïåğâîé çàäà÷åé ıòî òî, ÷òî öèêë äëèòñÿ, ïîêà êëş÷ ÁÎËÜØÅ ıëåìåíòîâ èç ëåâîé ÷àñòè
        arr[j + 1] = arr[j] 
        j -= 1
    arr[j + 1] = key 

output = open('output1.txt', 'w')

for el in arr:
    output.write(str(el))
    output.write(' ')

output.close()

end = time.perf_counter()

print(end - start)
