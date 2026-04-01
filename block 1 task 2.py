def calc_fib(n):                                #Итеративный алгоритм для подсчета числа
    if (n<=1):
        return n
    prev,curr=0,1
    for i in range(2,n+1):
        prev,curr = curr, prev+curr
    return curr

with open('input_1.2.txt', 'r') as file_in:     #Открытие входного файла для чтения
    n=int(file_in.readline())

result = calc_fib(n)

with open('output_1.2.txt','w') as file_out:    #Открытие выходного файла для записи
    file_out.write(str(result))
