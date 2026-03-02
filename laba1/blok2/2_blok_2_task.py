# -*- coding: utf-8 -*-
# 2
import time
import tracemalloc
tracemalloc.start()
time_start = time.perf_counter()
# ���� ��� ����� ��������� � ������ ��������, � �� ���� ��� ������ ���������

start = time.perf_counter()

file = open('input1.txt')

n = file.readline()

arr = list(map(int, file.readline().split()))

count = [1] # ������, � ������� ����� ��������� ������ �������

for i in range(1, len(arr)):
    key = arr[i] 
    j = i - 1

    while j >=0 and arr[j] > key:
        arr[j + 1] = arr[j] 
        j -= 1
    arr[j + 1] = key 
    count.append(j + 2) # �� ��� ������ �����, ������ ����� ���� ��� ����� ����� ��� ����� ��������� ������ � count. + 2 ��� ��� � ������ �������, ��� ��������� ���������� � 1, � �� � 0

output = open('output1.txt', 'w')

for el in count:
    output.write(str(el))
    output.write(' ')

for el in arr:
    output.write(str(el))
    output.write(' ')

output.close()

time_end = time.perf_counter()
print(f"Time to solve: {time_end - time_start:.5f} sec")
snapshot = tracemalloc.take_snapshot()
top_stats = snapshot.statistics("lineno")
total_size = sum(stat.size for stat in top_stats)
print("Total allocated size: %f MB" % (total_size / 10**6))
tracemalloc.stop()