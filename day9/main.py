def get_data():
    data = []
    with open("input.prod", "r") as f:
        data.extend(line.strip() for line in f.readlines())

    return data


def get_new_node_position(current, target):
    x_difference = target["x"] - current["x"]
    y_difference = target["y"] - current["y"]

    abs_x_difference = abs(x_difference)
    abs_y_difference = abs(y_difference)

    if abs_x_difference == 2:
        current["x"] += 1 if x_difference > 0 else -1
        if abs_y_difference == 1:
            current["y"] += y_difference

    if abs_y_difference == 2:
        current["y"] += 1 if y_difference > 0 else -1
        if abs_x_difference == 1:
            current["x"] += x_difference

    return current


def solution():
    data = get_data()
    rope = [{"x": 0, "y": 0} for _ in range(10)]

    visited_positions_part_1 = {
        (0, 0),
    }
    visited_positions_part_2 = {
        (0, 0),
    }
    for line in data:
        chunks = line.split()
        direction = chunks[0]
        steps = int(chunks[1])

        for _ in range(steps):
            if direction == "D":
                rope[0]["y"] -= 1
            elif direction == "L":
                rope[0]["x"] -= 1
            elif direction == "R":
                rope[0]["x"] += 1
            elif direction == "U":
                rope[0]["y"] += 1
            for node in range(1, len(rope)):
                new_position = get_new_node_position(rope[node], rope[node - 1])
                rope[node]["x"] = new_position["x"]
                rope[node]["y"] = new_position["y"]

            visited_positions_part_1.add((rope[1]["x"], rope[1]["y"]))
            visited_positions_part_2.add((rope[-1]["x"], rope[-1]["y"]))

    return len(visited_positions_part_1), len(visited_positions_part_2)


def main():
    print(f"Part 1: {solution()[0]}")
    print(f"Part 2: {solution()[1]}")


if __name__ == "__main__":
    main()
