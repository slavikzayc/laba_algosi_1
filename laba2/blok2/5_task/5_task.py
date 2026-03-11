import time
import tracemalloc
import random


def set_input(commands):
    with open("input.txt", 'w') as f:
        f.truncate()
        f.write(f"{len(commands)}\n")
        for command in commands:
            f.write(f"{command}\n")

def empty_stack_max():
    commands = ["push 1", "pop", "max"]
    set_input(commands)
def empty_stack_pop():
    commands = ["push 1", "pop", "max"]
    set_input(commands)
def monotonous_rising(count):
    commands = []
    for i in range(1, count):
        commands.append(f"push {i}")
    commands.append("max")
    set_input(commands)
def monotonous_falling(count):
    commands = []
    for i in range(count, 1, -1):
        commands.append(f"push {i}")
    commands.append("max")
    set_input(commands)
def equal_values(count):
    commands = []
    for _ in range(count):
        commands.append("push 5")
    commands.append("max")
    set_input(commands)
def alternating(count):
    commands = []
    for i in range(1, count + 1):
        commands.append(f"push {i}")
        if i % 3 == 0:
            commands.append("max")
        if i % 2 == 0:
            commands.append("pop")
    set_input(commands)
def random_commands(count):
    commands = []
    stack_size = 0

    for _ in range(count):
        if stack_size == 0:
            cmd_type = 'push'
        else:
            cmd_type = random.choice(['push', 'pop', 'max'])

        if cmd_type == 'push':
            value = random.randint(1, 100)
            commands.append(f"push {value}")
            stack_size += 1
        elif cmd_type == 'pop':
            commands.append("pop")
            stack_size -= 1
        else:
            commands.append("max")

    set_input(commands)
def large_numbers(count):
    commands = []
    for _ in range(count):
        value = random.randint(-10 ** 5, 10 ** 5)
        commands.append(f"push {value}")
    commands.append("max")
    set_input(commands)

# empty_stack_pop()
# empty_stack_max()
# monotonous_rising(400000)
# monotonous_falling(400000)
# equal_values(10)
# alternating(100)
# random_commands(10)

def parse_input(): #парсим файл
    with open("input.txt") as f:
        input_data = f.readlines()
        input_list = [i.strip() for i in input_data]
        commands_count = int(input_list[0])
        commands = input_list[1:]
        return commands_count, commands

tracemalloc.start()
time_start = time.perf_counter()

main_stack = [] #создаем основной стек
max_stack = [] #создаем вспомогательный стек максимумов
results = [] #массив для сохранения выводных данных

parsed_file = parse_input() #получаем данные из файла
commands = parsed_file[1] #сохраняем команды

for command in commands: #обрабатываем команды
    if command.startswith("push"): #если команда push
        _, value = command.split(' ')# то сплитим команду, строковую часть убираем в переменную _, а значение сохраняем
        value = int(value) #преобразуем значение
        main_stack.append(value) #добавляем в основной стек

        if not max_stack or value >= max_stack[-1]: #добавляем новый максимум, если такой появился
            max_stack.append(value)
        else:
            max_stack.append(max_stack[-1]) #если не появился, дублируем


    elif command == "pop":
        if main_stack:
            popped = main_stack.pop() #сохраняем удаленный элемент
            if popped == max_stack[-1]: #если он являлся максимумом
                max_stack.pop() #удаляем

    elif command == "max":
        if max_stack:
            results.append(str(max_stack[-1])) #в массив возвращаем последний максимум

time_end = time.perf_counter()
with open("output.txt", 'w') as f:
    f.truncate()
    f.write('\n'.join(results)) #записываем в файл


print(f"Time to solve: {time_end - time_start:.5f} sec")
snapshot = tracemalloc.take_snapshot()
top_stats = snapshot.statistics("lineno")
total_size = sum(stat.size for stat in top_stats)
print(f"Total allocated size: {total_size / 10 ** 6:.3f} MB")
tracemalloc.stop()