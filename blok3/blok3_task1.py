import time

start_time = time.perf_counter()

def legacy_merge(A, p, q, r):
    n1 = q - p + 1
    n2 = r - q

    L = [0] * (n1 + 1)
    R = [0] * (n2 + 1)

    for i in range(n1):
        L[i] = A[p + i]

    for j in range(n2):
        R[j] = A[q + 1 + j]

    L[n1] = float('inf')
    R[n2] = float('inf')

    i = 0
    j = 0

    for k in range(p, r + 1):
        if L[i] <= R[j]:
            A[k] = L[i]
            i += 1
        else:
            A[k] = R[j]
            j += 1

def legacy_merge_sort(A, p, r):
    if p < r:
        q = (p + r) // 2  # целочисленное деление (floor)
        legacy_merge_sort(A, p, q)
        legacy_merge_sort(A, q + 1, r)
        legacy_merge(A, p, q, r)
    return A

def merge(left_list, right_list):
    sorted_list = []
    left_list_index = right_list_index = 0
    left_list_length, right_list_length = len(left_list), len(right_list)

    for _ in range(left_list_length + right_list_length):
        if left_list_index < left_list_length and right_list_index < right_list_length:

            if left_list[left_list_index] <= right_list[right_list_index]:
                sorted_list.append(left_list[left_list_index])
                left_list_index += 1
            else:
                sorted_list.append(right_list[right_list_index])
                right_list_index += 1

        elif left_list_index == left_list_length:
            sorted_list.append(right_list[right_list_index])
            right_list_index += 1

        elif right_list_index == right_list_length:
            sorted_list.append(left_list[left_list_index])
            left_list_index += 1

    return sorted_list

def merge_sort(nums):

    if len(nums) <= 1:
        return nums

    mid = len(nums) // 2

    left_list = merge_sort(nums[:mid])
    right_list = merge_sort(nums[mid:])

    return merge(left_list, right_list)

list_of_numbers = [] #Создаем новый массив для считывания последовательности из файла
output_data = "" #Создаем строку для записи в файл

input_data = open("input.txt").readlines() #Читаем вводные данные
list_length = int(input_data[0]) #Из вводных данных считываем длину последовательности
raw_list_of_numbers = input_data[1].split(" ") #и саму последовательность в виде массива строк

for number in raw_list_of_numbers: #Проходим циклом по массиву строк
    list_of_numbers.append(int(number)) #Добавляем элементы в массив, где элементы уже будут типа int

list_of_numbers = legacy_merge_sort(list_of_numbers, 0, list_length-1) #Производим сортировку

for number in list_of_numbers: #Проходим циклом по отсортированному массиву
    output_data += str(number)+' ' #Добавляем отсортированную последовательность в строку

open("output.txt", 'a').write(output_data+'\n') #Записываем в файл

end_time = time.perf_counter()
execution_time = end_time - start_time
print(f"Время выполнения: {execution_time:.6f} секунд")

#При сортировке вставкой время может превышать 0,001 секунд, в то время как при
# сортировке слиянием оно не превышает 0,0004 секунды на данных:
# 10
# 999999999 888888888 888888888 777777777 666666666 555555555 444444444 333333333 222222222 111111111