# 1. There are multiple ranges of product IDs
# 2. Each range is separated by a comma in the day_2_input.txt file
# 3. Each range is defined by a start and end ID, separated by a hyphen
# 4. The task: find the invalid IDs by noticing the repeating of numbers in the
# sequence: for example, 11-22 has two invalid IDs, 11 and 22.
# 5. Next task: sum all the invalid IDs found in the ranges.
# 6. Note: no invalid IDs start with a 0.


def read_file_and_turn_to_list(file_path):
    with open(file_path, "r") as file:
        content = file.read().strip()
    return content.split(",")


def find_invalid_ids_in_range(start, end):
    """
    Finds the invalid product IDs in a given range.

    A product ID is considered invalid if it is an even length and
    the first half of the digits are the same as the second half.

    Parameters:
    start (int): The start of the range.
    end (int): The end of the range.

    Returns:
    list: A list of invalid product IDs.
    """
    invalid_ids = []
    for product_id in range(start, end + 1):
        str_id = str(product_id)
        if len(str_id) // 2 * 2 == len(str_id):  # Check if even length
            mid = len(str_id) // 2
            if str_id[:mid] == str_id[mid:]:
                invalid_ids.append(product_id)
    return invalid_ids


def sum_invalid_ids(file_path):
    ranges = read_file_and_turn_to_list(file_path)
    total_invalid_sum = 0

    for range_str in ranges:
        start_str, end_str = range_str.split("-")
        start, end = int(start_str), int(end_str)
        invalid_ids = find_invalid_ids_in_range(start, end)
        total_invalid_sum += sum(invalid_ids)

    return total_invalid_sum


if __name__ == "__main__":
    file_path = "data/day_2_input.txt"
    result = sum_invalid_ids(file_path)
    print(f"The sum of all invalid product IDs is: {result}")


# Part 2 rules:
# Now, an ID is invalid if it is made only of some sequence of digits repeated
# at least twice. So, 12341234 (1234 two times), 123123123 (123 three times),
# 1212121212 (12 five times), and 1111111 (1 seven times) are all invalid IDs.


def find_invalid_ids_part2_in_range(start, end):
    """
    Finds the invalid product IDs in a given range based on the new criteria.

    A product ID is considered invalid if it consists of a sequence of digits
    repeated at least twice.

    Parameters:
    start (int): The start of the range.
    end (int): The end of the range.

    Returns:
    list: A list of invalid product IDs.
    """
    invalid_ids = []
    for product_id in range(start, end + 1):
        str_id = str(product_id)
        length = len(str_id)
        for i in range(1, length // 2 + 1):
            if length % i == 0:
                if str_id[:i] * (length // i) == str_id:
                    invalid_ids.append(product_id)
                    break
    return invalid_ids


def sum_invalid_ids_part2(file_path):
    ranges = read_file_and_turn_to_list(file_path)
    total_invalid_sum = 0

    for range_str in ranges:
        start_str, end_str = range_str.split("-")
        start, end = int(start_str), int(end_str)
        invalid_ids = find_invalid_ids_part2_in_range(start, end)
        total_invalid_sum += sum(invalid_ids)

    return total_invalid_sum


if __name__ == "__main__":
    file_path = "data/day_2_input.txt"
    result_part2 = sum_invalid_ids_part2(file_path)
    print(f"The sum of all invalid product IDs for part 2 is: {result_part2}")
