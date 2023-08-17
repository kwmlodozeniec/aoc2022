import itertools
from string import ascii_lowercase


def get_data():
    with open("input.test", "r") as f:
        return [line.strip() for line in f.readlines()]


def walk_the_map(map_data):
    for row, column in itertools.product(range(len(map_data)), range(len(map_data[0]))):
        yield row, column, map_data[row][column]


def get_start_end(map_data):
    start, end = 0, 0

    for row, column, point_value in walk_the_map(map_data):
        if point_value == "S":
            start = (row, column)
        elif point_value == "E":
            end = (row, column)

    return start, end


def get_distance_map(map_data):
    return [[0] * len(map_data[0]) for _ in range(len(map_data))]


def set_distance_for_point(distance_map, point, distance):
    row, column = point
    distance_map[row][column] = distance


def get_point_value(map_data, point):
    row, column = point
    if column < 0 or row < 0:
        return None

    try:
        return map_data[row][column]
    except IndexError:
        print("Index error")
        return None


def get_distance_for_point(distance_map, point):
    row, column = point
    return distance_map[row][column]


def inspect_outsiders(map_data, point):
    row, column = point
    for outsider in ((column + 1, row + 0), (column - 1, row + 0), (column + 0, row + 1), (column + 0, row - 1)):
        if (value := get_point_value(map_data, outsider)) is not None:
            yield outsider, value


def can_go(current, target):
    transform = {
        "S": "a",
        "E": "z",
    }
    current = transform.get(current, current)
    target = transform.get(target, target)

    return ascii_lowercase.index(target) - ascii_lowercase.index(current)


def find_path(map_data, start, end):
    print(f"Starting point: {start}, looking for {end}")
    distance_map = get_distance_map(map_data)
    set_distance_for_point(distance_map, start, 1)

    visited_points = [start]
    current_point_index = -1

    while True:
        current_point_index += 1
        if current_point_index >= len(visited_points):
            break

        current_point = visited_points[current_point_index]
        print(current_point)

        if get_point_value(map_data, current_point) == end:
            print("We have reached the end")
            return get_distance_for_point(distance_map, current_point) - 1

        for outsider, point in inspect_outsiders(map_data, current_point):
            if can_go(get_point_value(map_data, current_point), get_point_value(map_data, outsider)) <= 1:
                visited_points.append(outsider)
                current_distance = get_distance_for_point(distance_map, current_point)
                set_distance_for_point(distance_map, outsider, current_distance + 1)


def part1():
    map_data = get_data()
    print(map_data)
    start, end = get_start_end(map_data)
    print(start, end)
    return find_path(map_data, start, get_point_value(map_data, end))


def main():
    print(f"Part 1: {part1()}")


if __name__ == "__main__":
    main()
