from functools import reduce


def get_data():
    data = []
    with open("input.prod", "r") as f:
        data.extend(line.strip() for line in f.readlines())

    grid = []
    for line in data:
        heights = [int(h) for h in list(line)]
        grid.append(heights)

    return grid


def is_tree_visible(grid, row, column, tree_height):
    print(f"Looking at tree [{row},{column}]:{grid[row][column]}")
    left = []
    right = []
    up = []
    down = []
    visible_trees_per_direction = []

    left.extend(grid[row][:column])
    right.extend(grid[row][column + 1 :])

    for row_idx in range(row):
        up.append(grid[row_idx][column])

    for row_idx in range(row + 1, len(grid)):
        down.append(grid[row_idx][column])

    print(left, right, up, down)

    visible_trees = 0
    for tree in left[::-1]:
        if tree < tree_height:
            visible_trees += 1
        if tree >= tree_height:
            visible_trees += 1
            break
    visible_trees_per_direction.append(visible_trees)

    visible_trees = 0
    for tree in right:
        if tree < tree_height:
            visible_trees += 1
        if tree >= tree_height:
            visible_trees += 1
            break
    visible_trees_per_direction.append(visible_trees)

    visible_trees = 0
    for tree in up[::-1]:
        if tree < tree_height:
            visible_trees += 1
        if tree >= tree_height:
            visible_trees += 1
            break
    visible_trees_per_direction.append(visible_trees)

    visible_trees = 0
    for tree in down:
        if tree < tree_height:
            visible_trees += 1
        if tree >= tree_height:
            visible_trees += 1
            break
    visible_trees_per_direction.append(visible_trees)

    score = reduce(lambda x, y: x * y, visible_trees_per_direction)

    print(f"Visible trees: {visible_trees_per_direction}, score: {score}")

    if max(left) < tree_height or max(right) < tree_height or max(up) < tree_height or max(down) < tree_height:
        return True, score

    return False, score


def main():
    data = get_data()
    for row in data:
        print(row)

    visible_trees = 0
    visible_trees += len(data) * 2
    visible_trees += len(data[0]) * 2 - 4

    scores = []

    for row_idx, row in enumerate(data):
        if row_idx in [0, len(data) - 1]:
            continue

        for column_idx, tree in enumerate(row):
            if column_idx in [0, len(row) - 1]:
                continue
            visible, score = is_tree_visible(data, row_idx, column_idx, tree)
            scores.append(score)
            if visible:
                print("Tree visible")
                visible_trees += 1
            else:
                print("Tree NOT visible")

    print(f"Part 1, visible trees: {visible_trees}")
    print(scores)
    print(f"Part 2: {max(scores)}")


if __name__ == "__main__":
    main()
