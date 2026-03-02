import time
import tracemalloc
import random
tracemalloc.start()
time_start = time.perf_counter()


def find_maximum_subarray(A):
    if not A:
        return 0, -1, -1

    # Инициализация
    global_max = A[0]  # максимальная сумма среди всех подмассивов
    current_max = A[0]  # максимальная сумма подмассива, заканчивающегося на текущем индексе

    # Для отслеживания границ
    start = 0
    end = 0
    temp_start = 0

    for i in range(1, len(A)):
        # Решаем, начать новый подмассив с A[i] или продолжить текущий
        if A[i] > current_max + A[i]:
            # Начинаем новый подмассив с текущего элемента
            current_max = A[i]
            temp_start = i
        else:
            # Продолжаем текущий подмассив
            current_max = current_max + A[i]

        # Обновляем глобальный максимум
        if current_max > global_max:
            global_max = current_max
            start = temp_start
            end = i

    return global_max, start, end

# Cтандартный случай
arr1 = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
sum1, start1, end1 = find_maximum_subarray(arr1)
print(f"Массив: {arr1}")
print(f"Максимальная сумма: {sum1}")
print(f"Подмассив: {arr1[start1:end1+1]}")
print(f"Индексы: [{start1}, {end1}]")

# Все положительные
arr2 = [1, 2, 3, 4, 5]
sum2, start2, end2 = find_maximum_subarray(arr2)
print(f"Массив: {arr2}")
print(f"Максимальная сумма: {sum2}")
print(f"Подмассив: {arr2[start2:end2+1]}")
print(f"Индексы: [{start2}, {end2}]")

# Все отрицательные
arr3 = [-5, -4, -3, -2, -1]
sum3, start3, end3 = find_maximum_subarray(arr3)
print(f"Массив: {arr3}")
print(f"Максимальная сумма: {sum3}")
print(f"Подмассив: {arr3[start3:end3+1]}")
print(f"Индексы: [{start3}, {end3}]")

time_end = time.perf_counter()
print(f"Time to solve: {time_end - time_start:.5f} sec")
snapshot = tracemalloc.take_snapshot()
top_stats = snapshot.statistics("lineno")
total_size = sum(stat.size for stat in top_stats)
print("Total allocated size: %f MB" % (total_size / 10 ** 6))
tracemalloc.stop()