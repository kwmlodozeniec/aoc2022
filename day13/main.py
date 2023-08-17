import enum
import itertools
from collections import UserList
from functools import total_ordering


@total_ordering
class Packet(UserList):
    def __eq__(self, otro):
        return self.data == otro.data if isinstance(otro, type(self)) else NotImplemented

    def __lt__(self, otro):
        return compare(self.data, otro.data) is Comparison.CORRECT if isinstance(otro, type(self)) else NotImplemented


class Comparison(enum.Enum):
    CORRECT = enum.auto()
    INCORRECT = enum.auto()
    NOT_COMPLETE = enum.auto()


def get_data():
    with open("input.prod", "r") as f:
        data = f.read().split("\n\n")
        packet_data = []
        for pair in data:
            packets = pair.split("\n")
            packet_data.append([eval(packets[0]), eval(packets[1])])
        return packet_data


def compare_ints(left, right):
    if left < right:
        return Comparison.CORRECT
    return Comparison.INCORRECT if left > right else Comparison.NOT_COMPLETE


def compare_lists(left, right):
    for _left, _right in itertools.zip_longest(left, right):
        if _left is None:
            return Comparison.CORRECT
        if _right is None:
            return Comparison.INCORRECT
        result = compare(_left, _right)
        if result == Comparison.NOT_COMPLETE:
            continue
        else:
            return result
    return Comparison.NOT_COMPLETE


def compare_mixed_types(left, right):
    if isinstance(left, int) and isinstance(right, list):
        return compare_lists([left], right)
    if isinstance(left, list) and isinstance(right, int):
        return compare_lists(left, [right])


def compare(left, right):
    print(f"Comparing {left} vs {right}")
    if isinstance(left, int) and isinstance(right, int):
        return compare_ints(left, right)
    if isinstance(left, list) and isinstance(right, list):
        return compare_lists(left, right)
    return compare_mixed_types(left, right)


def part1():
    data = get_data()
    ordered_indices = []
    for idx, line in enumerate(data):
        left, right = line
        if compare(left, right) == Comparison.CORRECT:
            print(f"Pair {idx+1} is in the right order")
            ordered_indices.append(idx + 1)

    print(ordered_indices)
    return sum(ordered_indices)


def part2():
    flat_list = []
    for line in get_data():
        left, right = line
        flat_list.extend((Packet(left), Packet(right)))

    divider_packet_a = Packet([[2]])
    divider_packet_b = Packet([[6]])

    flat_list.extend((divider_packet_a, divider_packet_b))
    flat_list.sort()

    return (flat_list.index(divider_packet_a) + 1) * (flat_list.index(divider_packet_b) + 1)


def main():
    print(f"Part 1: {part1()}")
    print(f"Part 2: {part2()}")


if __name__ == "__main__":
    main()
