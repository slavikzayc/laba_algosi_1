import time
import tracemalloc

tracemalloc.start()
time_start = time.perf_counter()

def parse_input(): #парсим файл
    with (open("input.txt") as f):
        input_data = f.readlines()
        nodes_count = int(input_data[0].strip())
        nodes_parents = [int(node_parent) for node_parent in input_data[1].split(' ')]
        return nodes_count, nodes_parents


print(parse_input())
time_end = time.perf_counter()
print(f"Time to solve: {time_end - time_start:.5f} sec")
snapshot = tracemalloc.take_snapshot()
top_stats = snapshot.statistics("lineno")
total_size = sum(stat.size for stat in top_stats)
print(f"Total allocated size: {total_size / 10 ** 6:.3f} MB")
tracemalloc.stop()