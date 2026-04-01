def is_fibonacci(num_str: str) -> bool:     #Функция проверяет, является ли переданное число числом Фибоначчи
    if not num_str or num_str[0] == '-':    #Если строка пустая или число отрицательное
        return False
    if num_str in ('0', '1'):               #0 и 1 - числа Фибоначчи
        return True

    try:
        n = int(num_str)                    #строка в целое число
        if n < 0:                           #если число отрицательное
            return False
    except ValueError:                      #если строка не является числом
        return False

    a, b = 0, 1
    while b < n:                            #итеративный подсчет чисел Фибоначчи
        a, b = b, a + b

    return b == n                           #после выхода из цикла если b = n, то это число Фибоначчи


try:
    with open('input.txt', 'r') as f:       #открытие файла для чтения
        lines = f.readlines()               #все строки файла в список

    N = int(lines[0].strip())               #первая строка - количество запросов
    results = []                            #пустой список для ответов

    for i in range(1, N + 1):
        num_str = lines[i].strip()          #берется одна строка из файла
        if is_fibonacci(num_str):           #проверка с помощью функции
            results.append("Yes")
        else:
            results.append("No")

    with open('output.txt', 'w') as f:
        f.write('\n'.join(results))         #все ответы записываются через перенос строки

    print("Готово! Результат записан в output.txt")

except FileNotFoundError:                   #если input.txt не найден
    print("Ошибка: файл input.txt не найден!")
except Exception as e:                      #если произошла иная ошибка
    print(f"Ошибка: {e}")