with open ('input_1.1.3.txt','r') as file_input:  #Открытие входного файла для чтения
    line=file_input.readline()  #Чтение строки
    a,b=map(int,line.split())  #Перевод строки в два числа

if -10**9<=a<=10**9 and -10**9<=b<=10**9:  #Проверка условия диапазона чисел
    result = a+b
else:
    result = 'Числа вне диапазона'

with open ('output_1.1.3.txt','w') as file_output:  #Открытие выходного файла для записи
    file_output.write(str(result))  #Запись результата в файл
