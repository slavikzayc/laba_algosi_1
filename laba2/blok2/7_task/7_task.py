import time
import tracemalloc

tracemalloc.start()
time_start = time.perf_counter()

from collections import deque

def moving_sequence(n, raw_sequence, m):
    window = deque()
    result = []

    for i in range(n):
        # Удаляем индексы, вышедшие за пределы окна
        if window and window[0] < i - m + 1:
            window.popleft()
        # Удаляем все индексы с меньшими значениями
        while window and raw_sequence[window[-1]] <= raw_sequence[i]:
            window.pop()
        window.append(i)
        # Как только окно закончилось, записываем максимум
        if i >= m - 1:
            result.append(raw_sequence[window[0]])
    return result


# Чтение входных данных
with open("input.txt", "r") as f:
    n = int(f.readline().strip())
    raw_sequence = list(map(int, f.readline().strip().split()))
    m = int(f.readline().strip())

result = moving_sequence(n, raw_sequence, m)

# Запись результата
with open("output.txt", "w") as f:
    f.write(" ".join(map(str, result)))


time_end = time.perf_counter()
print(f"Time to solve: {time_end - time_start:.5f} sec")
snapshot = tracemalloc.take_snapshot()
top_stats = snapshot.statistics("lineno")
total_size = sum(stat.size for stat in top_stats)
print(f"Total allocated size: {total_size / 10 ** 6:.3f} MB")
tracemalloc.stop()