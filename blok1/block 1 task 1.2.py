import time
import tracemalloc
tracemalloc.start()
time_start = time.perf_counter()

print('Введите число a и b')
a,b=map(int,input().split())        #Вход двух чисел a и b в одной строке
print(a+b**2)

time_end = time.perf_counter()
print(f"Time to solve: {time_end - time_start:.5f} sec")
snapshot = tracemalloc.take_snapshot()
top_stats = snapshot.statistics("lineno")
total_size = sum(stat.size for stat in top_stats)
print("Total allocated size: %f MB" % (total_size / 10**6))
tracemalloc.stop()
