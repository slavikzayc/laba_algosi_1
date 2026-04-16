def main():
    with open('input.txt', 'r') as f:       #открытие файла для чтения
        n = int(f.read().strip())

    if n == 1:                              #частный случай с n=1
        with open('output.txt', 'w') as f:
            f.write("0\n1")
        return

    dp = [0] * (n + 1)                      #массив для минимального количества операций

    for i in range(2, n + 1):               #заполнение массива, индекс - числовое значение, значение по индексу - кол-во операций для числа
        candidates = [dp[i - 1] + 1]        #список возможных способов получить число, операция +1
        if i % 2 == 0:                      #операция *2
            candidates.append(dp[i // 2] + 1)
        if i % 3 == 0:                      #оперция *3
            candidates.append(dp[i // 3] + 1)
        dp[i] = min(candidates)             #выбор минимального пути из числа операций

    sequence = []                           #массив для текущего числа
    while n > 1:                            #спуск от n до 1
        sequence.append(n)                  #каждое число для проверки начиная с максимального добавляется в массив
        if n % 3 == 0 and dp[n] == dp[n // 3] + 1: #поиск шага, который дал минимальный путь для n
            n //= 3
        elif n % 2 == 0 and dp[n] == dp[n // 2] + 1:
            n //= 2
        else:
            n -= 1
    sequence.append(1)                      #добавление первого элемента в конец

    sequence.reverse()                      #разворот последовательности

    with open('output.txt', 'w') as f:      #запись ответа
        f.write(str(len(sequence) - 1) + "\n")  #число операций для числа
        f.write(" ".join(map(str, sequence)))   #последовательность через пробел


if __name__ == "__main__":
    main()