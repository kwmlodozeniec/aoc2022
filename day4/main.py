def get_data(f="./input.txt"):
    data = []
    with open("input.prod", "r") as f:
        lines = f.readlines()
        data.extend(line.strip() for line in lines)
    return data


def get_sets(data):
    sets = []
    for line in data:
        left, right = line.split(",")
        left_min = int(left.split("-")[0])
        left_max = int(left.split("-")[-1])
        right_min = int(right.split("-")[0])
        right_max = int(right.split("-")[-1])

        left_set = set(list(range(left_min, left_max + 1)))
        right_set = set(list(range(right_min, right_max + 1)))
        sets.append((left_set, right_set))

    return sets


def main():
    data = get_data()
    overlapping_whole_sections = 0

    sets = get_sets(data)

    for pair in sets:
        if pair[0] - pair[1] == set() or pair[1] - pair[0] == set():
            overlapping_whole_sections += 1

    print(f"Part 1: {overlapping_whole_sections}")

    overlapping_partial_sections = 0
    for pair in sets:
        if pair[0].intersection(pair[1]):
            overlapping_partial_sections += 1

    print(f"Part 2: {overlapping_partial_sections}")


if __name__ == "__main__":
    main()
