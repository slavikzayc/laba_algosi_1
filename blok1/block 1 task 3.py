import time
import tracemalloc
tracemalloc.start()
time_start = time.perf_counter()

def last_fib(n):                                #Рекурсивная функция для подсчета числа
    if (n<=1):
        return n
    
    n = n%60                                    #Период Пизано, при котором последние цифры
                                                  #последовательности повторяются с периодом 60
    if n<=1:                                    #Вычисление чисел Фибоначчи
        return n
    fib_prev,fib_curr=0,1                       
    for i in range (2,n+1):                     
        fib_next=(fib_prev+fib_curr)%10         #Последняя цифра нового числа последовательности
        fib_prev=fib_curr                       #Текущее становится предыдущим
        fib_curr=fib_next                       #Новая цифра становится текущей
    return fib_curr

with open('input_1.3.txt', 'r') as file_in:     #Открытие входного файла для чтения
    n=int(file_in.readline())

result = last_fib(n)

with open('output_1.3.txt', 'w') as file_out:    #Открытие выходного файла для записи
    file_out.write(str(result))

time_end = time.perf_counter()
print(f"Time to solve: {time_end - time_start:.5f} sec")
snapshot = tracemalloc.take_snapshot()
top_stats = snapshot.statistics("lineno")
total_size = sum(stat.size for stat in top_stats)
print("Total allocated size: %f MB" % (total_size / 10**6))
tracemalloc.stop()