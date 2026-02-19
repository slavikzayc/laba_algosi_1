def calc_fib(n):                                #Рекурсивная функция для подсчета числа
    if (n<=1):
        return n
    return calc_fib(n-1)+calc_fib(n-2)

with open('input_1.2.txt', 'r') as file_in:     #Открытие входного файла для чтения
    n=int(file_in.readline())

result = calc_fib(n)

with open('output_1.2.txt','w') as file_out:    #Открытие выходного файла для записи
    file_out.write(str(result))
