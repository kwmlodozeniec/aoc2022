import string

letters_array = string.ascii_letters


def get_data():
    data = []
    with open("input.prod", "r") as f:
        lines = f.readlines()
        data.extend(line.strip() for line in lines)
    return data


def get_total(letters):
    return sum(letters_array.index(letter) + 1 for letter in letters)


def main():
    data = get_data()

    common_items = []
    for line in data:
        first_compartment = line[: int(len(line) / 2)]
        second_compartment = line[int(len(line) / 2) :]
        common = set(first_compartment).intersection(set(second_compartment))
        common_items.extend(list(common))

    print(f"Part 1: {get_total(common_items)}")

    badge_items = []
    for _ in range(len(data) // 3):
        firts = set(data.pop(0))
        second = set(data.pop(0))
        third = set(data.pop(0))
        common = firts & second & third
        badge_items.extend(list(common))

    print(f"Part 2: {get_total(badge_items)}")


if __name__ == "__main__":
    main()
