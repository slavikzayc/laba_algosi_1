with open ('input_1.1.3.txt','r') as file_input:  #Открытие входного файла для чтения
    line=file_input.readline()  #Чтение строки
    numbers=list(map(int,line.split()))

if len(numbers)==2:
    a,b=numbers[0],numbers[1]
    result = a+b
    with open ('output_1.1.3.txt','w') as file_output:  
        file_output.write(str(result))
else:
    print('Ошибка')
