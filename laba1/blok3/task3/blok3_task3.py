import time
import tracemalloc
import random
tracemalloc.start()
time_start = time.perf_counter()

inversions_count = 0

def merge_and_count(left_list, right_list):
    global inversions_count
    merged = []
    i = j = 0
    left_list_length, right_list_length = len(left_list), len(right_list)

    while i < left_list_length and j < right_list_length: # алгоритм сортировки слиянием
        if left_list[i] <= right_list[j]:
            merged.append(left_list[i])
            i += 1
        else:
            inversions_count += left_list_length - i #но если элемент из правой части меньше, добавляем количество оставшихся элементов
            # из левого отсортированного массива, тк элемент из правого образует с ними инверсию
            merged.append(right_list[j])
            j += 1
#n(n-1)/2
    merged.extend(left_list[i:])
    merged.extend(right_list[j:])

    return merged

def count_inversions(nums):
    if len(nums) <= 1: # базовый случай рекурсии
        return nums
    mid = len(nums) // 2 # находим индекс среднего элемента
    left_list = count_inversions(nums[:mid]) # получаем левую отсортированную часть
    right_list = count_inversions(nums[mid:]) # получаем правую отсортированную часть

    return merge_and_count(left_list, right_list) # возвращаем результат слияния левой и правой частей

def get_input(filename):
    list_of_numbers = []
    with open(filename) as f:  # читаем файл
        input_data = f.readlines()

    list_length = int(input_data[0].strip())  #
    raw_list_of_numbers = input_data[1].strip().split()  # обрабатываем строки

    for number in raw_list_of_numbers:
        if number:  # проверяем, что строка не пустая
            list_of_numbers.append(int(number))
    return [list_length, list_of_numbers]

def set_input(count):
    with open("input.txt", 'w') as f:
        # очищаем файл от предыдущих данных
        f.truncate(0)
        # Записываем количество чисел
        f.write(f"{count}\n")
        # Генерируем числа в случайном порядке
        unique_numbers = random.sample(range(-(10**9)+1, 10**9), count)
        # Перемешиваем для гарантии случайного порядка
        # Записываем числа через пробел
        f.write(' '.join(map(str, unique_numbers)))

def set_output(inversions):
    with open("output.txt", 'w') as f:
        # очищаем файл от предыдущих данных
        # Записываем количество инверсий
        f.write(f"{inversions}\n")

set_input(100000)
count_inversions(get_input("input.txt")[1])
set_output(inversions_count)

# Проверка алгоритма
# inversions_arr = count_inversions(get_input("input.txt")[1]) #считаем количество инверсий и записываем отсортированную последовательность
# prev = inversions_count #сохраняем количество инверсий
# count_inversions(inversions_arr) #считаем количество инверсий с необнуленным счетчиком
# if prev == inversions_count: #количество инверсий не изменилось => 0 инверсий в отсортированной последовательности
#     print("no inversions in sorted list")
# set_output(inversions_count)

time_end = time.perf_counter()
print(f"Time to solve: {time_end - time_start:.5f} sec")
snapshot = tracemalloc.take_snapshot()
top_stats = snapshot.statistics("lineno")
total_size = sum(stat.size for stat in top_stats)
print("Total allocated size: %f MB" % (total_size / 10 ** 6))
tracemalloc.stop()

# Time to solve: 0.85727 sec
# Total allocated size: 0.012407 MB