import time
import tracemalloc

tracemalloc.start()
time_start = time.perf_counter()

def parse_input(): #парсим файл
    with open("input.txt") as f:
        input_data = f.readlines()
        nodes_data = int(input_data[0].strip())
        nodes_parents_data = [int(node_parent) for node_parent in input_data[1].split()]
        return nodes_data, nodes_parents_data

n, parents = parse_input()  # Вызывает функцию парсинга и распаковывает возвращаемые значения в переменные

# Находим корень
root = 0
for i in range(n):  # Проходим по всем индексам узлов
    if parents[i] == -1:  # Если родитель узла -1
        root = i  # Запоминаем индекс корня
        break

children = [[] for _ in range(n)]  # Создаем список из n пустых списков для хранения детей каждого узла
for i in range(n):  # Проходим по всем узлам
    if parents[i] != -1:  # Если у узла есть родитель
        children[parents[i]].append(i)  # Добавляем текущий узел в список детей его родителя

stack = [(root, 1)]  # Создаем стек
max_height = 1  # Инициализируем переменную максимальной высоты дерева

while stack:  # Пока стек не пуст
    node, depth = stack.pop()  # Извлекаем последний добавленный узел и его глубину из стека
    if depth > max_height:  # Если текущая глубина больше найденной максимальной
        max_height = depth  # Обновляем максимальную высоту
    for child in children[node]:  # Перебираем всех детей текущего узла
        stack.append((child, depth + 1))  # Добавляем каждого ребенка в стек с увеличенной на 1 глубиной

with open("output.txt", "w") as f:
    f.write(str(max_height))
time_end = time.perf_counter()
print(f"Time to solve: {time_end - time_start:.5f} sec")
snapshot = tracemalloc.take_snapshot()
top_stats = snapshot.statistics("lineno")
total_size = sum(stat.size for stat in top_stats)
print(f"Total allocated size: {total_size / 10 ** 6:.3f} MB")
tracemalloc.stop()