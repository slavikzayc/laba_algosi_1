import sys


def main():
    with open('input.txt', 'r', encoding='utf-8') as infile, \
            open('output.txt', 'w', encoding='utf-8') as outfile:

        lines = infile.read().strip().splitlines()

        # m — количество сегментов
        m = int(lines[0])
        # n — количество запросов
        n = int(lines[1])

        # Создаём пустые цепочки (списки) для каждого сегмента
        table = [[] for _ in range(m)]

        p = 100000007
        x = 263

        # Хеш-функция
        def get_hash(s):
            h = 0
            power = 1
            for ch in s:
                h = (h + ord(ch) * power) % p
                power = (power * x) % p
            # возвращаем номер сегмента
            return h % m

        output = []

        # Обрабатываем запросы (начинаются со строки с индексом 2)
        for i in range(2, n + 2):
            parts = lines[i].split()
            cmd = parts[0]

            if cmd == 'add':
                s = parts[1]
                h = get_hash(s)
                # Вставляем в начало, если ещё нет
                if s not in table[h]:
                    table[h].insert(0, s)

            elif cmd == 'del':
                s = parts[1]
                h = get_hash(s)
                # Удаляем, если есть
                if s in table[h]:
                    table[h].remove(s)

            elif cmd == 'find':
                s = parts[1]
                h = get_hash(s)
                output.append('yes' if s in table[h] else 'no')

            elif cmd == 'check':
                idx = int(parts[1])
                # Выводим цепочку через пробел, если не пуста
                if table[idx]:
                    output.append(' '.join(table[idx]))
                else:
                    output.append('')

        # Записываем все результаты в файл
        outfile.write('\n'.join(output))


if __name__ == '__main__':
    main()