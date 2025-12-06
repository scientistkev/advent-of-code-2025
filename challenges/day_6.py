# The Elves in the kitchen explain the situation: because of their complicated new inventory management system, they can't figure out which of their ingredients are fresh and which are spoiled. When you ask how it works, they give you a copy of their database (your puzzle input).

# The database operates on ingredient IDs. It consists of a list of fresh ingredient ID ranges, a blank line, and a list of available ingredient IDs. For example:

# 3-5
# 10-14
# 16-20
# 12-18

# 1
# 5
# 8
# 11
# 17
# 32
# The fresh ID ranges are inclusive: the range 3-5 means that ingredient IDs 3, 4, and 5 are all fresh. The ranges can also overlap; an ingredient ID is fresh if it is in any range.

# The Elves are trying to determine which of the available ingredient IDs are fresh. In this example, this is done as follows:

# Ingredient ID 1 is spoiled because it does not fall into any range.
# Ingredient ID 5 is fresh because it falls into range 3-5.
# Ingredient ID 8 is spoiled.
# Ingredient ID 11 is fresh because it falls into range 10-14.
# Ingredient ID 17 is fresh because it falls into range 16-20 as well as range 12-18.
# Ingredient ID 32 is spoiled.
# So, in this example, 3 of the available ingredient IDs are fresh.

# Process the database file from the new inventory management system. How many of the available ingredient IDs are fresh?


def load_data(path):
    with open(path, "r") as f:
        fresh_ranges_str, available_ids_str = f.read().strip().split("\n\n")
    fresh_ranges = []
    for line in fresh_ranges_str.split("\n"):
        start, end = map(int, line.split("-"))
        fresh_ranges.append((start, end))
    available_ids = list(map(int, available_ids_str.split("\n")))
    return fresh_ranges, available_ids


def count_fresh_ids(fresh_ranges, available_ids):
    fresh_count = 0
    for ingredient_id in available_ids:
        for start, end in fresh_ranges:
            if start <= ingredient_id <= end:
                fresh_count += 1
                break
    return fresh_count


def main():
    fresh_ranges, available_ids = load_data("data/day_6_input.txt")
    fresh_count = count_fresh_ids(fresh_ranges, available_ids)
    print(f"Number of fresh ingredient IDs: {fresh_count}")


if __name__ == "__main__":
    main()
