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


# The Elves start bringing their spoiled inventory to the trash chute at the back of the kitchen.

# So that they can stop bugging you when they get new inventory, the Elves would like to know all of the IDs that the fresh ingredient ID ranges consider to be fresh. An ingredient ID is still considered fresh if it is in any range.

# Now, the second section of the database (the available ingredient IDs) is irrelevant. Here are the fresh ingredient ID ranges from the above example:

# 3-5
# 10-14
# 16-20
# 12-18
# The ingredient IDs that these ranges consider to be fresh are 3, 4, 5, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, and 20. So, in this example, the fresh ingredient ID ranges consider a total of 14 ingredient IDs to be fresh.

# Process the database file again. How many ingredient IDs are considered to be fresh according to the fresh ingredient ID ranges?


def merge_ranges(fresh_ranges):
    sorted_ranges = sorted(fresh_ranges, key=lambda x: x[0])
    merged_ranges = []
    current_start, current_end = sorted_ranges[0]

    for start, end in sorted_ranges[1:]:
        if start <= current_end + 1:
            current_end = max(current_end, end)
        else:
            merged_ranges.append((current_start, current_end))
            current_start, current_end = start, end

    merged_ranges.append((current_start, current_end))
    return merged_ranges


def count_total_fresh_ids(fresh_ranges):
    merged_ranges = merge_ranges(fresh_ranges)
    total_fresh_count = 0
    for start, end in merged_ranges:
        total_fresh_count += end - start + 1
    return total_fresh_count


def main():
    fresh_ranges, _ = load_data("data/day_6_input.txt")
    total_fresh_count = count_total_fresh_ids(fresh_ranges)
    print(f"Total number of fresh ingredient IDs: {total_fresh_count}")


if __name__ == "__main__":
    main()
