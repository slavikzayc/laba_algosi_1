import time
import tracemalloc
import random



def parse_input(): #парсим файл
    with open("input.txt") as f:
        input_data = f.readlines()
        input_list = [i.strip() for i in input_data]
        commands_count = int(input_list[0])
        commands = input_list[1:]
        return commands_count, commands

parsed_file=parse_input()
commands = parsed_file[1]
tracemalloc.start()
time_start = time.perf_counter()

stack_in = []
stack_out = []
output = []

for command in commands:
    if command.startswith('+'): #если команда +
        _, value = command.split(' ')# то сплитим команду, строковую часть убираем в переменную _, а значение сохраняем
        value = int(value) #преобразуем значение
        if not stack_in: #если стек входных значений пустой
            stack_in.append((value, value)) #добавляем кортеж, с элементом, и минимумом на этот момент (это же число)
        else:
            current_min_in = stack_in[-1][1] #берем последний минимум из последнего кортежа
            stack_in.append((value, min(value, current_min_in))) #добавляем новый кортеж из полученного элемента и минимума на данный момент
    elif command == '-':
        if not stack_out: #если выходной стек пустой
            while stack_in: # перекладываем значения в обратном порядке, пока входной стек не пустой
                value, _ = stack_in.pop()
                if not stack_out:#если выходной стек пустой
                    stack_out.append((value, value))#добавляем значение, и его же как минимальное
                else:
                    current_min_out = stack_out[-1][1]#фиксируем минимум на данный момент
                    stack_out.append((value, min(value, current_min_out)))#добавляем в выходной стек значение и минимальное значение на данный момент
        if stack_out:
            stack_out.pop() #в случае, если входной стек пустой, просто удаляем последний элемент из выходного стека
    elif command == '?':
        # Берём минимум из stack_in (если есть) или бесконечность
        min_in = stack_in[-1][1] if stack_in else float('inf')
        # Берём минимум из stack_out (если есть) или бесконечность
        min_out = stack_out[-1][1] if stack_out else float('inf')
        # Настоящий минимум — наименьший из двух
        current_min = min(min_in, min_out)
        # По условию задачи очередь не пуста, но на всякий случай:
        if current_min == float('inf'):
            output.append("Empty queue")  # или можно просто ничего не делать
        else:
            output.append(str(current_min))
        #записываем вывод
time_end = time.perf_counter()
with open("output.txt", 'w') as f:
    f.truncate()
    f.write('\n'.join(output)) #записываем в файл


print(f"Time to solve: {time_end - time_start:.5f} sec")
snapshot = tracemalloc.take_snapshot()
top_stats = snapshot.statistics("lineno")
total_size = sum(stat.size for stat in top_stats)
print(f"Total allocated size: {total_size / 10 ** 6:.3f} MB")
tracemalloc.stop()