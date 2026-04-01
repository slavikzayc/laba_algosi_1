import time
import tracemalloc
from collections import deque


def parse_input():
    with open("input.txt", "r") as f:
        first_line = f.readline().split()
        S = int(first_line[0])
        n = int(first_line[1])
        packets = []
        for _ in range(n):
            line = f.readline()
            if not line:
                break
            A, P = map(int, line.split())
            packets.append((A, P))
    return S, n, packets


def process_packets(buffer_size, packets):
    # очередь времен окончания обработки
    finish_times = deque()
    # список результатов
    results = []

    for arrival_time, processing_time in packets:
        # удаляем завершенные пакеты
        while finish_times and finish_times[0] <= arrival_time:
            finish_times.popleft()
        # проверяем переполнение буфера
        if len(finish_times) == buffer_size:
            results.append(-1)
            continue
        # вычисляем время начала обработки
        if not finish_times:
            start_time = arrival_time
        else:
            start_time = max(arrival_time, finish_times[-1])

        # обновляем очередь и результаты
        finish_time = start_time + processing_time
        finish_times.append(finish_time)
        results.append(start_time)

    return results


def write_input_to_file(buffer_size, packets, filename="input.txt"):
    with open(filename, "w") as f:
        f.write(f"{buffer_size} {len(packets)}\n")
        for arrival, processing in packets:
            f.write(f"{arrival} {processing}\n")


def write_output_to_file(results, filename="output.txt"):
    with open(filename, "w") as f:
        for result in results:
            f.write(str(result) + "\n")


def test_single_packet():
    buffer_size = 1
    packets = [(0, 1)]
    write_input_to_file(buffer_size, packets)


def test_buffer_overflow():
    buffer_size = 1
    packets = [(0, 1), (0, 1)]
    write_input_to_file(buffer_size, packets)


def test_packets_during_processing():
    buffer_size = 2
    packets = [(0, 5), (1, 1), (2, 1)]
    write_input_to_file(buffer_size, packets)


def test_large_delay():
    buffer_size = 2
    packets = [(0, 1), (100, 1), (101, 1)]
    write_input_to_file(buffer_size, packets)


def test_complex_scenario():
    buffer_size = 2
    packets = [(0, 3), (1, 2), (2, 1), (4, 2), (5, 1)]
    write_input_to_file(buffer_size, packets)

# test_single_packet()
test_buffer_overflow()
# test_packets_during_processing()
# test_large_delay()
# test_complex_scenario()

S, n, packets = parse_input()
results = process_packets(S, packets)
write_output_to_file(results)