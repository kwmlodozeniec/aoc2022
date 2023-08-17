def get_data(filename):
    data = []
    with open(filename, "r") as f:
        data = f.read()

    return data.split("\n\n")


def get_totals(data):
    totals = []
    for line in data:
        numbers = [int(number) for number in line.strip().split("\n")]
        totals.append(sum(numbers))
    return totals


def part1(filename):
    totals = get_totals(get_data(filename))

    max_total_index = max(range(len(totals)), key=totals.__getitem__)
    max_total = totals[max_total_index]
    print(f"Elf index with highest count {max_total_index}, count {max_total}")
    return max_total


def part2(filename):
    totals = get_totals(get_data(filename))
    top_three = 0
    for _ in range(3):
        max_total_index = max(range(len(totals)), key=totals.__getitem__)
        top_three += totals[max_total_index]
        totals.pop(max_total_index)

    print(f"Top three counts sum {top_three}")
    return top_three


def main():
    part1("input.prod")
    part2("input.prod")


if __name__ == "__main__":
    main()
