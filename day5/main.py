from collections import defaultdict


def get_data():
    with open("input.prod", "r") as f:
        stacks, process = f.read().split("\n\n")

    stacks = stacks.splitlines()[:-1]
    process_temp = process.splitlines()

    stacks = [x[1::4] for x in stacks]

    valid_stacks = defaultdict(list)

    for stack in stacks[::-1]:
        for idx, c in enumerate(list(stack)):
            if c != " ":
                valid_stacks[idx + 1].append(c)

    process = []
    for p in process_temp:
        _, crates, _, source, _, destination = p.strip().split(" ")
        process.append([int(crates), int(source), int(destination)])

    return valid_stacks, process


def part1():
    stacks, process = get_data()
    print(f"Stack before: {stacks}")
    print(f"Process: {process}")

    for line in process:
        crates, source, destination = line
        print(f"Moving {crates} from {source} to {destination}")
        for _ in range(crates):
            crate = stacks[source].pop()
            stacks[destination].append(crate)

    print(f"Stack after: {stacks}")

    answer = [stacks[idx + 1][-1] for idx in range(len(stacks)) if stacks[idx + 1]]
    print(f"Part 1: {''.join(answer)}")


def part2():
    stacks, process = get_data()
    print(f"Stack before: {stacks}")
    print(f"Process: {process}")

    for line in process:
        crates, source, destination = line
        print(f"Moving {crates} from {source} to {destination}")
        cargo = stacks[source][len(stacks[source]) - crates :]
        stacks[destination].extend(cargo)
        for _ in range(crates):
            stacks[source].pop()

    print(f"Stack after: {stacks}")

    answer = [stacks[idx + 1][-1] for idx in range(len(stacks)) if stacks[idx + 1]]
    print(f"Part 2: {''.join(answer)}")


def main():
    part1()
    part2()


if __name__ == "__main__":
    main()
