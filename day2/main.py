def decode_part_one(text):
    decoded = text
    decoded = decoded.replace("A", "rock")
    decoded = decoded.replace("X", "rock")
    decoded = decoded.replace("B", "paper")
    decoded = decoded.replace("Y", "paper")
    decoded = decoded.replace("C", "scissors")
    decoded = decoded.replace("Z", "scissors")
    return decoded


def decode_part_two(text):
    decoded = text
    decoded = decoded.replace("A", "rock")
    decoded = decoded.replace("X", "lose")
    decoded = decoded.replace("B", "paper")
    decoded = decoded.replace("Y", "draw")
    decoded = decoded.replace("C", "scissors")
    decoded = decoded.replace("Z", "win")
    return decoded


move_points = {
    "rock": 1,
    "paper": 2,
    "scissors": 3,
}


def get_specified_outcome_point(text):
    their_move, outcome = text.split(" ")
    if outcome == "draw":
        return get_result_point(text.replace(outcome, their_move))

    if outcome == "win":
        if their_move == "rock":
            return get_result_point(text.replace(outcome, "paper"))
        elif their_move == "paper":
            return get_result_point(text.replace(outcome, "scissors"))
        else:
            return get_result_point(text.replace(outcome, "rock"))
    elif outcome == "lose":
        if their_move == "rock":
            return get_result_point(text.replace(outcome, "scissors"))
        elif their_move == "paper":
            return get_result_point(text.replace(outcome, "rock"))
        else:
            return get_result_point(text.replace(outcome, "paper"))


def get_result_point(text):
    their_move, our_move = text.split(" ")

    if their_move == our_move:
        return 3 + move_points[our_move]  # draw
    if our_move == "rock":
        if their_move == "paper":
            return 0 + move_points[our_move]  # loss
    elif our_move == "paper":
        if their_move == "scissors":
            return 0 + move_points[our_move]  # loss
    elif our_move == "scissors":
        if their_move == "rock":
            return 0 + move_points[our_move]  # loss
    return 6 + move_points[our_move]  # win


def get_data(filename):
    data = []
    with open(filename, "r") as f:
        lines = f.readlines()
        data.extend(line.strip() for line in lines)
    return data


def main():
    total = sum(get_result_point(decode_part_one(line)) for line in get_data())
    print(f"Total score: {total}")

    total_set_outcome = sum(get_specified_outcome_point(decode_part_two(line)) for line in get_data())  # type: ignore
    print(f"Total with set outcome: {total_set_outcome}")


if __name__ == "__main__":
    main()
