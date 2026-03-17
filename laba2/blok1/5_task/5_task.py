"""
Median-QuickSort (медиана трёх).

Задание: реализовать QuickSort, где pivot выбирается как медиана из трёх элементов:
первый, средний, последний (в текущем массиве/подмассиве), и сравнить с:
1) обычным QuickSort (pivot = последний)
2) randomized QuickSort (pivot = случайный)

Ниже — максимально простой учебный вариант: НЕ in-place.
Он делает разбиение на 3 списка (меньше/равно/больше pivot) и рекурсивно сортирует части.
"""

from __future__ import annotations  # включает "отложенные" аннотации типов (удобно для list[int] и т.п.)

import random  # модуль случайных чисел (нужен для randomized pivot и генерации тестовых данных)
import time  # модуль времени (нужен для замеров скорости)
from typing import Callable  # Callable нужен, чтобы типизировать "функцию выбора pivot"


def _median3(a: int, b: int, c: int) -> int:  # функция для медианы из трёх чисел
    """Возвращает медиану (среднее по величине) из трёх чисел a, b, c."""  # докстрока: что делает функция

    if a <= b:  # если a не больше b
        if b <= c:  # если b не больше c, то порядок a <= b <= c
            return b  # медиана тут b (среднее значение)
        if a <= c:  # иначе b > c, но если a <= c, то порядок a <= c < b
            return c  # медиана тут c
        return a  # иначе порядок c < a <= b, медиана тут a
    else:  # иначе a > b
        if a <= c:  # если a <= c, то порядок b < a <= c
            return a  # медиана тут a
        if b <= c:  # иначе a > c, но если b <= c, то порядок b <= c < a
            return c  # медиана тут c
        return b  # иначе порядок c < b < a, медиана тут b


def _quicksort(arr: list[int], choose_pivot: Callable[[list[int]], int]) -> list[int]:  # общий QuickSort
    """Общий QuickSort: choose_pivot(arr) должен вернуть pivot-значение."""  # что ожидаем от choose_pivot

    if len(arr) <= 1:  # база рекурсии: массив из 0/1 элемента уже отсортирован
        return arr[:]  # возвращаем копию (arr[:] = новый список), чтобы не менять входной arr

    pivot = choose_pivot(arr)  # выбираем опорный элемент (pivot) по заданной стратегии

    less: list[int] = []  # сюда будем складывать элементы строго меньше pivot
    equal: list[int] = []  # сюда будем складывать элементы равные pivot
    greater: list[int] = []  # сюда будем складывать элементы строго больше pivot

    for x in arr:  # одним проходом разбрасываем элементы по 3 спискам
        if x < pivot:  # если x меньше pivot
            less.append(x)  # кладём x в список "less"
        elif x > pivot:  # иначе если x больше pivot
            greater.append(x)  # кладём x в список "greater"
        else:  # иначе значит x == pivot
            equal.append(x)  # кладём x в список "equal"

    # Рекурсивно сортируем "less" и "greater" и склеиваем: (отсортированное less) + equal + (отсортированное greater)
    return _quicksort(less, choose_pivot) + equal + _quicksort(greater, choose_pivot)  # итоговая склейка


def quicksort(arr: list[int]) -> list[int]:  # обычный QuickSort
    """Обычный QuickSort: pivot = последний элемент."""  # описание стратегии

    return _quicksort(arr, lambda a: a[-1])  # pivot берём как последний элемент текущего (под)массива


def randomized_quicksort(arr: list[int], seed: int | None = 0) -> list[int]:  # randomized QuickSort
    """Randomized-QuickSort: pivot = случайный элемент."""  # описание стратегии

    rnd = random.Random(seed)  # создаём отдельный генератор случайных чисел (не трогаем глобальный random)
    return _quicksort(arr, lambda a: a[rnd.randrange(len(a))])  # pivot — случайный элемент из текущего (под)массива


def median_quicksort(arr: list[int]) -> list[int]:  # median-of-three QuickSort
    """Median-QuickSort: pivot = медиана трёх (первый/средний/последний)."""  # описание стратегии

    def choose(a: list[int]) -> int:  # внутренняя функция выбора pivot для текущего (под)массива a
        mid = len(a) // 2  # индекс среднего элемента (для длины 5 это 2; для длины 4 это 2 тоже)
        return _median3(a[0], a[mid], a[-1])  # pivot-значение = медиана из (первый, средний, последний)

    return _quicksort(arr, choose)  # запускаем общий QuickSort с нашей стратегией pivot


def _make_datasets(n: int, seed: int = 0) -> dict[str, list[int]]:  # генерация тестовых наборов
    """Несколько типов входных данных для сравнения."""  # что генерируем

    rnd = random.Random(seed)  # отдельный RNG, чтобы генерация данных была повторяемой
    base = [rnd.randrange(0, n**3) for _ in range(n)]  # случайный массив длины n из диапазона [0, n^3)

    sorted_data = sorted(base)  # полностью отсортированный массив (часто "плохой" случай для pivot=последний)
    reversed_data = sorted_data[::-1]  # тот же массив, но в обратном порядке

    almost = sorted_data[:]  # почти отсортированный: начинаем с отсортированного и немного "портим" порядок
    swaps = max(1, n // 50)  # количество случайных перестановок (примерно 2% элементов)
    for _ in range(swaps):  # выполняем swaps перестановок
        i = rnd.randrange(n)  # случайный индекс i
        j = rnd.randrange(n)  # случайный индекс j
        almost[i], almost[j] = almost[j], almost[i]  # меняем элементы местами

    many_dups = [rnd.randrange(0, max(2, n // 10)) for _ in range(n)]  # много повторов (узкий диапазон значений)

    return {  # возвращаем словарь: имя набора -> список данных
        "random": base,  # полностью случайные данные
        "sorted": sorted_data,  # уже отсортированные данные
        "reversed": reversed_data,  # отсортированные в обратном порядке
        "almost_sorted": almost,  # почти отсортированные
        "many_duplicates": many_dups,  # много одинаковых элементов
    }  # конец словаря


def _time_once(fn: Callable[[list[int]], list[int]], data: list[int]) -> float:  # замер времени
    """Время одного запуска fn(data) в секундах."""  # описание

    t0 = time.perf_counter()  # старт таймера (высокоточный)
    _ = fn(data)  # запускаем сортировку (результат нам не нужен, нужен только замер времени)
    return time.perf_counter() - t0  # возвращаем разницу (сколько заняло)


def compare_sorts(n: int = 3000, repeats: int = 3) -> None:  # сравнение алгоритмов
    """Печатает сравнение 3 вариантов QuickSort на разных данных."""  # описание

    datasets = _make_datasets(n)  # генерируем наборы данных

    algos: list[tuple[str, Callable[[list[int]], list[int]]]] = [  # список алгоритмов: (название, функция)
        ("QuickSort(last)", quicksort),  # обычный QuickSort
        ("QuickSort(random)", lambda a: randomized_quicksort(a, seed=0)),  # randomized QuickSort (seed фиксируем)
        ("QuickSort(median3)", median_quicksort),  # median-of-three QuickSort
    ]  # конец списка algos

    print(f"n={n}, repeats={repeats}")  # печатаем параметры эксперимента
    for name, data in datasets.items():  # перебираем все наборы данных
        print(f"\nDATASET: {name}")  # печатаем имя набора
        for algo_name, algo_fn in algos:  # перебираем алгоритмы
            times = [_time_once(algo_fn, data) for _ in range(repeats)]  # запускаем repeats раз и собираем времена
            best = min(times)  # лучшее (минимальное) время
            avg = sum(times) / repeats  # среднее время
            print(f"{algo_name:18} best={best:.6f}s avg={avg:.6f}s")  # печатаем результаты красиво в строку


if __name__ == "__main__":  # точка входа: этот блок выполнится только при запуске файла напрямую
    compare_sorts(n=3000, repeats=3)  # запускаем сравнение (можно менять n/repeats под свой ПК)
