def get_data():
    with open("input.prod", "r") as f:
        return f.read().strip()


def find_position(offset):
    data = list(get_data())

    for idx, letter in enumerate(list(data)):
        if len(set(data[idx : idx + offset])) == offset:
            return idx + offset


def main():
    print(f"Part 1: {find_position(4)}")
    print(f"Part 2: {find_position(14)}")


if __name__ == "__main__":
    main()
