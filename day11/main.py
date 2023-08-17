from dataclasses import dataclass
from typing import List


def get_data():
    with open("input.prod", "r") as f:
        return f.read().split("\n\n")


@dataclass()
class Monkey:
    items: list
    operation: str
    operation_number: str
    diviser: int
    true_condition_monkey: int
    false_condition_monkey: int
    inspected_items: int
    large_worry_lcm: int


def prodess_data():
    data = get_data()

    monkeys = []

    for line in data:
        lines = [l.strip().rstrip() for l in line.split("\n")]
        items = [int(item) for item in lines[1].split("items: ")[-1].split(", ")]
        operation, number = lines[2].split("old ")[-1].split()
        diviser = int(lines[3].split(" by ")[-1])
        if_true = int(lines[4].split("throw to monkey ")[-1])
        if_false = int(lines[5].split("throw to monkey ")[-1])

        monkeys.append(
            Monkey(
                items=items,
                operation=operation,
                operation_number=number,
                diviser=diviser,
                true_condition_monkey=if_true,
                false_condition_monkey=if_false,
                inspected_items=0,
                large_worry_lcm=0,
            )
        )

    return monkeys


def solution(rounds, divide=True):
    monkeys: List[Monkey] = prodess_data()

    worry_lcm = 1
    for monkey in monkeys:
        worry_lcm *= monkey.diviser
    for monkey in monkeys:
        monkey.large_worry_lcm = worry_lcm

    for _ in range(rounds):
        for monkey_idx, monkey in enumerate(monkeys):
            # print(f"Processing monkey {monkey_idx} {monkey}")
            for idx, item in enumerate(monkey.items):
                monkey.inspected_items += 1
                operation_number = (
                    int(monkey.operation_number) if monkey.operation_number.isdigit() else int(monkey.items[idx])
                )

                worry = 0
                if monkey.operation == "*":
                    worry = item * operation_number
                elif monkey.operation == "+":
                    worry = item + operation_number

                if monkey.large_worry_lcm:
                    worry %= monkey.large_worry_lcm

                if divide:
                    worry //= 3

                condition = worry % monkey.diviser == 0
                if condition:
                    # print(
                    #     f"Throwing item {idx}:{monkey.items[idx]} from {monkey_idx} to {monkey.true_condition_monkey}"
                    # )
                    monkeys[monkey.true_condition_monkey].items.append(worry)
                else:
                    # print(
                    #     f"Throwing item {idx}:{monkey.items[idx]} from {monkey_idx} to {monkey.false_condition_monkey}"
                    # )
                    monkeys[monkey.false_condition_monkey].items.append(worry)

            monkey.items = []

    inspected_items_rankings = [monkey.inspected_items for monkey in monkeys]
    print(inspected_items_rankings)
    inspected_items_rankings.sort(reverse=True)
    return inspected_items_rankings[0] * inspected_items_rankings[1]


def main():
    print(f"Part 1: {solution(20)}")
    print(f"Part 2: {solution(10000,divide=False)}")


if __name__ == "__main__":
    main()
