import time
import tracemalloc
import random

tracemalloc.start()
time_start = time.perf_counter()

#1.1 Реализация алгоритма сортировки слиянием на основе псевдокода из лекции
def legacy_merge(A, p, q, r):  # A - последовательность, pqr - индексы элементов последовательности
    n1 = q - p + 1  # Длина левой части
    n2 = r - q  # Длина правой части

    L = [0] * (n1 + 1)  # Массив длины n1+1
    R = [0] * (n2 + 1)  # Массив длины n2+1

    # Копируем элементы во временные массивы
    for i in range(n1):
        L[i] = A[p + i]
    for j in range(n2):
        R[j] = A[q + 1 + j]

    L[n1] = float('inf')  #
    R[n2] = float('inf')  # Добавляем последним элементом массивов L и R ограничители

    i = j = 0
    # Слияние в исходный массив
    for k in range(p, r + 1): # запускаем цикл от первого индекса до последнего
        if L[i] <= R[j]: # если элемент из левой части меньше или равен элементу из правой части
            A[k] = L[i] # вставляем в исходный массив
            i += 1 # сдвигаемся на следующий элемент в левой части
        else:
            A[k] = R[j] # вставляем в исходный массив элемент из правой части
            j += 1 # сдвигаемся на следующий элемент в правой части
def legacy_merge_sort(A, p, r):
    if p < r:
        q = (p + r) // 2
        legacy_merge_sort(A, p, q)  # сортируем левую половину
        legacy_merge_sort(A, q + 1, r)  # сортируем правую половину
        legacy_merge(A, p, q, r)  # cливаем отсортированные половины
    return A
#1.2 Проверка алгоритма
# функция, реализующая сортировку и вывод по входным данным из файла,
def sort_with_file(filename):
    list_of_numbers = []
    output_data = ""

    with open(filename) as f: # читаем файл
        input_data = f.readlines()

    list_length = int(input_data[0].strip()) #
    raw_list_of_numbers = input_data[1].strip().split() # обрабатываем строки

    for number in raw_list_of_numbers:
        if number:  # проверяем, что строка не пустая
            list_of_numbers.append(int(number))

    list_of_numbers = legacy_merge_sort(list_of_numbers, 0, list_length-1)

    for number in list_of_numbers:
        output_data += str(number) + ' '

    with open("output.txt", 'w') as f:
        f.write(output_data + '\n')
# тесты
def test_on_bad_data(count): # функция, тестирующая пул данных худшего случая, зависимых от аргумента(количество элементов, т.е. чисел порядка 10^9) для сортировки)
    with open("test_input.txt", 'w') as f:
        # очищаем файл от предыдущих данных
        f.truncate(0)
        # записываем количество чисел
        f.write(f"{count}\n")

        # записываем числа в порядке убывания
        for i in range(count):
            number = 10 ** 9 - i
            f.write(str(number))
            if i < count - 1:
                f.write(' ')
    #cортируем
    sort_with_file("test_input.txt")
def test_on_good_data(count): #функция, тестирующая набор отсортированных данных в порядке неубывания
    with open("test_input.txt", 'w') as f:
        # очищаем файл от предыдущих данных
        f.truncate(0)
        # записываем количество чисел
        f.write(f"{count}\n")
        # записываем числа в порядке возрастания
        for i in range(count):
            number = (10**9)-count+i
            f.write(str(number))
            if i < count - 1:
                f.write(' ')
    #cортируем
    sort_with_file("test_input.txt")
def test_on_mid_data(count): #функция, тестирующая средний случай (неотсортированный набор случайных данных)
    with open("test_input.txt", 'w') as f:
        # очищаем файл от предыдущих данных
        f.truncate(0)
        # Записываем количество чисел
        f.write(f"{count}\n")

        # Генерируем числа в случайном порядке (средний случай)
        numbers = []
        for i in range(count):
            # Генерируем случайные числа в диапазоне около 10^9
            number = random.randint(-(10 ** 9)+1, (10 ** 9)-1)
            numbers.append(number)

        # Перемешиваем для гарантии случайного порядка
        random.shuffle(numbers)

        # Записываем числа через пробел
        f.write(' '.join(map(str, numbers)))
    sort_with_file("test_input.txt")

#test_on_bad_data(1000) заняло 0.01177 секунд и использовало 0.007404 МБ памяти сортировкой слиянием, сортировкой вставкой 0.15834 секунд, 0.040422 МБ
#test_on_bad_data(10000) заняло 0.15237 секунд и использовало 0.009469 МБ памяти сортировкой слиянием, сортировкой вставкой 21.02223 секунд, 0.368742 МБ
#test_on_bad_data(100000) заняло 1.79261 секунд и использовало 0.010813 МБ памяти сортировкой слиянием, сортировкой вставкой >10 минут

#test_on_good_data(1000) заняло 0.01516 секунд и использовало 0.007548 МБ памяти сортировкой слиянием, сортировкой вставкой 0.00220 секунд, 0.040446 МБ
#test_on_good_data(10000) заняло 0.015589 секунд и использовало 0.009613 МБ памяти сортировкой слиянием, сортировкой вставкой 0.02110 секунд, 0.368766 МБ
#test_on_good_data(100000) заняло 1.78764 секунд и использовало 0.010957 МБ памяти сортировкой слиянием, сортировкой вставкой 0.16362 секунд, 3.504574 МБ

#test_on_mid_data(1000) заняло 0.01324 секунд и использовало 0.010361 МБ памяти сортировкой слиянием, сортировкой вставкой 0.10589 секунд, 0.040450 МБ
#test_on_mid_data(10000) заняло 0.17028 секунд и использовало 0.013606 МБ памяти сортировкой слиянием, сортировкой вставкой 10.70793 секунд, 0.368746 МБ
#test_on_mid_data(100000) заняло 1.97642 секунд и использовало 0.014950 МБ памяти сортировкой слиянием, сортировкой вставкой >10 минут

#1.3 Переписанные процедуры
def merge(left_list, right_list):
    sorted_list = []
    i = j = 0
    left_list_length, right_list_length = len(left_list), len(right_list)

    for _ in range(left_list_length + right_list_length): # запускаем цикл по общему количеству элементов в обоих массивах
        if i < left_list_length and j < right_list_length: # проверяем, что не дошли до конца обоих списков
            if left_list[i] <= right_list[j]: # если элемент меньше или равен элементу из правой части
                sorted_list.append(left_list[i]) # добавляем в новый массив
                i += 1 # сдвигаемся на следующий элемент в левой части
            else:
                sorted_list.append(right_list[j]) # добавляем элемент из правой части в новый массив
                j += 1 # сдвигаемся на следующий элемент в правой части
        elif i == left_list_length: # проверяем, что в левой части закончились элементы
            sorted_list.append(right_list[j]) # добавляем из правой части
            j += 1 # сдвигаемся на следующий элемент в правой части
        elif j == right_list_length: # проверяем, что в правой части закончились элементы
            sorted_list.append(left_list[i]) # добавляем элемент из левой части
            i += 1 # сдвигаемся на следующий элемент в левой части

    return sorted_list
def merge_sort(nums):
    if len(nums) <= 1: # базовый случай рекурсии
        return nums

    mid = len(nums) // 2 # находим индекс среднего элемента

    left_list = merge_sort(nums[:mid]) # получаем левую отсортированную часть
    right_list = merge_sort(nums[mid:]) # получаем правую отсортированную часть

    return merge(left_list, right_list) # возвращаем результат слияния левой и правой частей

#sort_with_file("input.txt") по требованию в задании

time_end = time.perf_counter()
print(f"Time to solve: {time_end - time_start:.5f} sec")
snapshot = tracemalloc.take_snapshot()
top_stats = snapshot.statistics("lineno")
total_size = sum(stat.size for stat in top_stats)
print("Total allocated size: %f MB" % (total_size / 10 ** 6))
tracemalloc.stop()