# Day 4 Challenge: Finding optimal joltage
# 1. We are given a grid of numbers representing joltage ratings
# Ex: 987654321111111  -> jotalge = 98
#     811111111111119  -> jotalge = 89
#     234234234234278. -> jotalge = 78
#     818181911112111  -> jotalge = 92
# 2. For each line we need to find the combination of numbers that gives the
# highest joltage.
# 2b. For example in 987654321111111 the highest joltage is 98 (the highest two
# digit number)
# 3. We need to return the sum of the highest joltage from each line.
# Note: you cannot rearrange the battery order (no sorting of digits allowed).
# Logic: search for tens digit that isn't the last digit in the line,
# then find the highest digit after it to form the highest two digit number.


def search_for_tens_digit_number(line: str) -> int:
    max_joltage = 0
    for i in range(len(line) - 1):
        tens_digit = line[i]
        for j in range(i + 1, len(line)):
            units_digit = line[j]
            joltage = int(tens_digit + units_digit)
            if joltage > max_joltage:
                max_joltage = joltage
    return max_joltage


def calculate_total_joltage(file_path: str) -> int:
    total_joltage = 0
    with open(file_path, "r") as file:
        for line in file:
            line = line.strip()
            if line:
                max_joltage = search_for_tens_digit_number(line)
                total_joltage += max_joltage
    return total_joltage


if __name__ == "__main__":
    print("The total joltage is:", calculate_total_joltage("data/day_4_input.txt"))


# Now, you need to make the largest joltage by turning on exactly twelve batteries within each bank.

# The joltage output for the bank is still the number formed by the digits of the batteries you've turned on; the only difference is that now there will be 12 digits in each bank's joltage output instead of two.

# Consider again the example from before:

# 987654321111111
# 811111111111119
# 234234234234278
# 818181911112111
# Now, the joltages are much larger:

# In 987654321111111, the largest joltage can be found by turning on everything except some 1s at the end to produce 987654321111.
# In the digit sequence 811111111111119, the largest joltage can be found by turning on everything except some 1s, producing 811111111119.
# In 234234234234278, the largest joltage can be found by turning on everything except a 2 battery, a 3 battery, and another 2 battery near the start to produce 434234234278.
# In 818181911112111, the joltage 888911112111 is produced by turning on everything except some 1s near the front.
# LOGIC: We need to find the largest 12-digit number by selecting digits in order from the string.
# HOWEVER when it comes to the 12th digit we want to make sure we have the largest possible digit


def search_for_twelve_digit_joltage(line: str) -> int:
    target_len = 12
    n = len(line)

    if n < target_len:
        raise ValueError(
            f"Line too short ({n} digits), need at least {target_len}: {line}"
        )

    chosen_digits = []
    start = 0
    remaining = target_len

    print(f"  Searching best {target_len}-digit subsequence in: {line}")

    while remaining > 0:
        # Last index we can start from and still have enough digits left
        end = n - remaining  # inclusive

        # Look at the window line[start : end+1] and pick the largest digit
        window = line[start : end + 1]
        max_digit = max(window)
        # Earliest occurrence of this max digit in the window
        offset = window.index(max_digit)
        idx = start + offset

        chosen_digits.append(max_digit)
        print(
            f"    Picked digit {max_digit} at position {idx}; "
            f"window was [{start}:{end + 1}) = {window}"
        )

        # Move start past the chosen index
        start = idx + 1
        remaining -= 1

    joltage = int("".join(chosen_digits))
    print(f"  Max joltage for this line: {joltage}")
    return joltage


def calculate_total_twelve_digit_joltage(file_path: str) -> int:
    total_joltage = 0
    with open(file_path, "r") as file:
        for line_num, line in enumerate(file, 1):
            line = line.strip()
            if line:
                print(f"\nLine {line_num}: {line}")
                max_joltage = search_for_twelve_digit_joltage(line)
                total_joltage += max_joltage
                print(f"Running total: {total_joltage}")
    return total_joltage


if __name__ == "__main__":
    print(
        "The total twelve-digit joltage is:",
        calculate_total_twelve_digit_joltage("data/day_4_input.txt"),
    )
