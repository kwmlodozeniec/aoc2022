from collections import defaultdict


def get_data():
    data = []
    with open("input.prod", "r") as f:
        data.extend(line.strip() for line in f.readlines())
    return data


def get_file_structure():
    data = get_data()
    filesystem = []

    location = []
    paths = []
    for line in data:
        if "$" in line:
            if "cd /" in line:  # reset location to root
                location = [""]
            elif "cd .." in line:  # go up one directory
                location.pop()
            elif "cd " in line:  # go to directory
                dir_name = line.split("cd ")[-1]
                location.append(dir_name)
            elif "ls" in line:  # list directory
                paths.append(f"{'/'.join(location)}/")
        else:
            if "dir" in line:
                continue
            else:
                file_size, file_name = line.split(" ")
                filesystem.append(f"{'/'.join(location)}/{file_name}-{file_size}")

    return paths, filesystem


def get_path_sizes(paths, filesystem):
    path_sizes = defaultdict(lambda: 0)
    for p in paths:
        matching_files = [f for f in filesystem if p in f]
        total_size = sum(int(f.split("-")[-1]) for f in matching_files)
        path_sizes[p] = total_size

    return path_sizes


def get_total_sum(size_threshold, path_sizes):
    return sum(v for k, v in path_sizes.items() if v <= size_threshold)


def get_size_of_deletion_candidate(path_sizes):
    TOTAL_SPACE = 70_000_000
    SPACE_REQUIRED = 30_000_000

    available_space = TOTAL_SPACE - path_sizes["/"]
    additional_space_required = SPACE_REQUIRED - available_space

    candidates = [v for k, v in path_sizes.items() if v >= additional_space_required]

    return min(candidates)


def main():
    paths, filesystem = get_file_structure()
    path_sizes = get_path_sizes(paths, filesystem)
    print(f"Part 1: {get_total_sum(100_000, path_sizes)}")
    print(f"Part 2: {get_size_of_deletion_candidate(path_sizes)}")


if __name__ == "__main__":
    main()
