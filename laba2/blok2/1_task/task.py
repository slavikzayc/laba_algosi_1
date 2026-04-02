stack = [] # массив для стека, сюда добавляем элементы и отсюда убираем их

file = open('input.txt')

n = int(file.readline())

lines = [l for l in file.readlines()] # массив всех операций

file.close()

output = open('output.txt', 'w')

for i in range(n):
    line = lines[i].split() # вот тут мы берем операцию, split нужен для разделения операции и значения(если оно есть)

    if line[0] == '+': # вот тут мы добавляем в стэк элементы, если операция подходит
        stack.append(line[1])
    else:
        print(str(stack.pop()), file=output) # вот тут мы берем последний элемент из стэка

output.close()

