import time
import tracemalloc
tracemalloc.start()
time_start = time.perf_counter()

with open ('input_1.1.3.txt', 'r') as file_input:  #Открытие входного файла для чтения
    line=file_input.readline()  #Чтение строки
    a,b=map(int,line.split())  #Перевод строки в два числа

result = a+b

with open ('output_1.1.3.txt', 'w') as file_output:  #Открытие выходного файла для записи
    file_output.write(str(result))  #Запись результата в файл

time_end = time.perf_counter()
print(f"Time to solve: {time_end - time_start:.5f} sec")
snapshot = tracemalloc.take_snapshot()
top_stats = snapshot.statistics("lineno")
total_size = sum(stat.size for stat in top_stats)
print("Total allocated size: %f MB" % (total_size / 10**6))
tracemalloc.stop()