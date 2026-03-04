queuee = [] # массив  для очереди

file = open('input.txt')

n = int(file.readline())

lines = [l for l in file.readlines()] # массив операций

file.close()

output = open('output.txt', 'w')

for i in range(n):
    line = lines[i].split() # берем нашу операцию, так же делим на саму операцию и значение

    if line[0] == '+': # добавляем "справа элемент"
        queuee.append(line[1])
    else:
        print(str(queuee.pop(0)), file=output) # убираем "слева" элемент


