def get_data():
    with open("input.prod", "r") as f:
        return [line.strip() for line in f.readlines()]


def check_cycle(cycle):
    cycles_of_interest = [20, 60, 100, 140, 180, 220]

    return cycle in cycles_of_interest


def part1():
    data = get_data()
    X = 1

    cycle = 0
    signal_strengths = []
    for line in data:
        cycle += 1
        if check_cycle(cycle):
            print(f"Cycle {cycle}, X is {X}")
            signal_strengths.append(X * cycle)

        if "noop" not in line:
            _, value = line.split()
            value = int(value)
            cycle += 1
            if check_cycle(cycle):
                print(f"Cycle {cycle}, X is {X}")
                signal_strengths.append(X * cycle)
            X += value

    print(f"Part 1: {sum(signal_strengths)}")


def part2():
    data = get_data()

    cycle = 0
    sprite_cycles = [0, 1, 2]
    image = ["." for _ in range(240)]

    for line in data:
        cycle += 1
        print(cycle, sprite_cycles)
        if (cycle - 1) % 40 in sprite_cycles:
            print(f"Drawing pixel {cycle-1}")
            image[cycle - 1] = "#"

        if "noop" not in line:
            _, value = line.split()
            value = int(value)
            cycle += 1
            print(cycle, sprite_cycles)
            if (cycle - 1) % 40 in sprite_cycles:
                print(f"Drawing pixel {cycle-1}")
                image[cycle - 1] = "#"

            sprite_cycles = [x + value for x in sprite_cycles]

    lines = [image[:40], image[40:80], image[80:120], image[120:160], image[160:200], image[200:240]]

    for line in lines:
        print("".join(line))


def main():
    part1()
    part2()


if __name__ == "__main__":
    main()
