import time
import tracemalloc

def build_palindrome(s):
    povtor = [0] * 26  # массив для подсчета букв (A-0, B-1, ..., Z-25)

    # Подсчет количества каждой буквы
    for char in s:
        povtor[ord(char) - ord('A')] += 1

    # Поиск лучшего центрального элемента
    left = []
    center = ''
    max_odd = 0
    center_index = -1

    # Сначала найдем букву с максимальным нечетным количеством для центра
    for i in range(26):
        if povtor[i] % 2 != 0 and povtor[i] > max_odd:
            max_odd = povtor[i]
            center_index = i

    # Если нашли нечетную букву, делаем ее центром
    if center_index != -1:
        center = chr(ord('A') + center_index)
        povtor[center_index] -= 1  # убираем одну букву для центра

    # Строим левую часть из оставшихся букв (в алфавитном порядке)
    for i in range(26):
        if povtor[i] > 0:
            left.append(chr(ord('A') + i) * (povtor[i] // 2))

    left = ''.join(left)
    return left + center + left[::-1]


def process_input(filename):
    try:
        with open(filename, 'r') as file:
            # Чтение первой строки
            first_line = file.readline().strip()
            if not first_line:
                return "Ошибка: файл пустой"

            # Проверка числа n
            try:
                n = int(first_line)
                if n < 1 or n > 100000:
                    return "Ошибка: n должно быть в интервале от 1 до 100000 включительно"
            except ValueError:
                return "Ошибка: n должно быть целым числом"

            # Чтение строки с буквами
            s = file.readline().strip()

            # Специальная проверка для n=1
            if n == 1:
                if len(s) != 1:
                    return f"Ошибка: при n=1 ожидается 1 символ, получено {len(s)}"
                if not ('A' <= s[0] <= 'Z'):
                    return "Ошибка: символ должен быть заглавной латинской буквой"
                return s  # для одной буквы палиндром - это сама буква

            # Общая проверка для остальных случаев
            if not s:
                return "Ошибка: строка пустая"

            if len(s) != n:
                return f"Ошибка: ожидалось {n} символов, получено {len(s)}"

            # Проверка символов
            invalid_chars = []
            for c in s:
                if not ('A' <= c <= 'Z'):
                    invalid_chars.append(c)

            if invalid_chars:
                return f"Ошибка: недопустимые символы: {', '.join(invalid_chars)}"

            # Если все проверки пройдены - строим палиндром
            return build_palindrome(s)

    except FileNotFoundError:
        return "Ошибка: файл не найден"
    except Exception as e:
        return f"Неожиданная ошибка: {e}"


# Основная программа
time_start = time.perf_counter()
tracemalloc.start()

result = process_input('input.txt')

with open('output.txt', 'w') as output:
    output.write(result)

time_end = time.perf_counter()
print(f"Time to solve: {time_end - time_start:.5f} sec")

snapshot = tracemalloc.take_snapshot()
top_stats = snapshot.statistics("lineno")
total_size = sum(stat.size for stat in top_stats)
print("Total allocated size: %f MB" % (total_size / 10 ** 6))
tracemalloc.stop()