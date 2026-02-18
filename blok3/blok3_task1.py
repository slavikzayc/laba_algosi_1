import time

start_time = time.perf_counter()

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

list_of_numbers = merge_sort(list_of_numbers) #Производим сортировку

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