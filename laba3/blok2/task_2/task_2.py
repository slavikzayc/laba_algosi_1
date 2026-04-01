file = open('input.txt')

n = int(file.readline())

arr = dict()

for i in range(n):
    stroka = [str(a) for a in file.readline().split()] # получаем команду

    if stroka[0] == 'add':
        # ключ - номер, значение - имя
        arr[stroka[1]] = stroka[2]
    elif stroka[0] == 'del':
        # если есть номер то удаляем, иначе игнорируем
        if stroka[1] in arr.keys():
            del arr[stroka[1]]
    else:
        # если нашли номер, то выводим, иначе "not found"
        if stroka[1] in arr.keys():
            print(arr[stroka[1]])
        else:
            print('not found')