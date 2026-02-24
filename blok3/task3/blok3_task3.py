import time
import tracemalloc
import random
tracemalloc.start()
time_start = time.perf_counter()

#модифицировать сортировку слиянием, посчитать количество инверсий в массиве из 1<n<10^5 чисел не превосходящих 10^5

def get_input(filename):


time_end = time.perf_counter()
print(f"Time to solve: {time_end - time_start:.5f} sec")
snapshot = tracemalloc.take_snapshot()
top_stats = snapshot.statistics("lineno")
total_size = sum(stat.size for stat in top_stats)
print("Total allocated size: %f MB" % (total_size / 10 ** 6))
tracemalloc.stop()