import math


filename = "input.txt"


def parse_and_get_records_part_1(filename):
    with open(filename) as file:
        times = file.readline()
        times = times.split(':')[1].strip().split()
        times = [int(n) for n in times]

        distances = file.readline()
        distances = distances.split(':')[1].strip().split()
        distances = [int(n) for n in distances]

        records = dict(zip(times, distances))
        return records


def parse_and_get_records_part_2(filename):
    with open(filename) as file:
        time = file.readline()
        time = time.split(':')[1].replace(" ", "")
        time = int(time)

        distance = file.readline()
        distance = distance.split(':')[1].replace(" ", "")
        distance = int(distance)

        records = {time: distance}
        return records


records = parse_and_get_records_part_2(filename)


win_counts = []
for [time, distance] in records.items():

    times_won = 0

    for speed in range(1, time):
        time_left = time - speed

        dist_travelled = time_left * speed

        if dist_travelled > distance:
            times_won += 1

    win_counts.append(times_won)

print(math.prod(win_counts))
