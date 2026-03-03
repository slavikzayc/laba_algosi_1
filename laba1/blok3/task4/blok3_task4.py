import time
import tracemalloc
import random

tracemalloc.start()
time_start = time.perf_counter()

def set_input(count):
    with open("input.txt", 'w') as f:
        # очищаем файл от предыдущих данных
        f.truncate(0)
        # Записываем количество чисел
        start = random.randint(1, 10)
        step = random.randint(1, 5)

        sorted_list = [start + i * step for i in range(count)]

        # Генерируем числа для поиска (могут быть как в списке, так и нет)
        to_find_count = random.randrange(1, count)  # сколько чисел ищем
        nums_to_find = []

        for _ in range(to_find_count):
            # С вероятностью 50% берем число из списка, 50% - случайное
            if random.choice([True, False]) and sorted_list:
                # Берем случайное число из существующего списка
                nums_to_find.append(random.choice(sorted_list))
            else:
                # Генерируем случайное число (может попасть в список, а может нет)
                # Берем диапазон шире, чем в списке
                min_val = start - step * 2
                max_val = start + (count + 2) * step
                nums_to_find.append(random.randint(min_val, max_val))

        f.write(f"{count} ")
        f.write(' '.join(map(str, sorted_list)))
        f.write("\n")
        f.write(f"{to_find_count} ")
        f.write(' '.join(map(str, nums_to_find)))

def read(filename):
    with open(filename) as f:  # читаем файл
        input_data = f.readlines()
        input_list = [int(s) for s in input_data[0].strip().split()]  # обрабатываем строки
        input_to_find = [int(s) for s in input_data[1].strip().split()]
        return input_list[1:], input_to_find[1:]

def set_output(results):
    with open("output.txt", 'w') as f:
        # очищаем файл от предыдущих данных
        # Записываем количество инверсий
        f.write(' '.join(map(str, results)))

def binary_search(A, B):
    results = []  # список для результатов

    for item in B:  # проходим по всем элементам из B
        low = 0
        high = len(A) - 1
        found = False  # флаг, нашли ли элемент

        while low <= high:
            mid = (low + high) // 2
            guess = A[mid]

            if guess == item:
                results.append(mid)  # добавляем индекс
                found = True
                break
            if guess > item:
                high = mid - 1
            else:
                low = mid + 1

        if not found:  # если не нашли элемент
            results.append(-1)  # добавляем -1

    return results

set_input(100000)
set_output(binary_search(read("input.txt")[0], read("input.txt")[1]))

time_end = time.perf_counter()
print(f"Time to solve: {time_end - time_start:.5f} sec")
snapshot = tracemalloc.take_snapshot()
top_stats = snapshot.statistics("lineno")
total_size = sum(stat.size for stat in top_stats)
print("Total allocated size: %f MB" % (total_size / 10 ** 6))
tracemalloc.stop()