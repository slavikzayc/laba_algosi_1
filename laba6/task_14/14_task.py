import sys

def solve():
    data = sys.stdin.read().strip().split()
    if not data:
        return

    it = iter(data)
    num_villages = int(next(it))
    start_village = int(next(it))
    target_village = int(next(it))
    num_trips = int(next(it))

    trips = []
    for _ in range(num_trips):
        from_village = int(next(it))
        dep_time = int(next(it))
        to_village = int(next(it))
        arr_time = int(next(it))
        trips.append((from_village, dep_time, to_village, arr_time))

    INF = 10 ** 9
    earliest_arrival = [INF] * (num_villages + 1)
    earliest_arrival[start_village] = 0  # в начальный момент 0 мы уже в start_village

    # не более num_villages - 1 пересадок
    for _ in range(num_villages - 1):
        # копия, чтобы обновления одной итерации не влияли на другие обновления в этой же итерации
        updated_arrival = earliest_arrival[:]
        for from_v, dep, to_v, arr in trips:
            # можем уехать, если уже находимся в деревне отправления к моменту отправления
            if earliest_arrival[from_v] <= dep and arr < updated_arrival[to_v]:
                updated_arrival[to_v] = arr
        earliest_arrival = updated_arrival

    if earliest_arrival[target_village] == INF:
        print(-1)
    else:
        print(earliest_arrival[target_village])


if __name__ == '__main__':
    solve()