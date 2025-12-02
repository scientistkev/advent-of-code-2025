# 1. Lock starts at position p
# 2. The lock can move a distance d
# 3. The lock can move in two directions: left (L) and right (R), -d or +d
# 3a. If there were no wraparound, p+d is the new position when moving right (R)
# 3b. If there were no wraparound, p-d is the new position when moving left (L)
# 4. The position changes with wraparound:
#   - If moving right and p+d > 99, the new position is (p + d) % 100
#   - If moving left and p-d < 0, the new position is (p - d) % 100
# 5. If the new position is 0, count it
# 6. If the dial passes 0 at any point during the move, count it


def parse_direction(instruction):
    direction = instruction[0]
    if direction not in ("L", "R"):
        raise ValueError("Invalid direction; must be 'L' or 'R'")
    else:
        return direction


def parse_distance(instruction):
    distance = int(instruction[1:])
    return distance


def translate_direction_into_movement(direction, distance):
    if direction == "R":
        return distance
    elif direction == "L":
        return -distance
    else:
        raise ValueError("Invalid direction; must be 'L' or 'R'")


def count_zero_positions(instructions):
    position = 50
    zero_count = 0

    if instructions is None:
        raise ValueError("Instructions cannot be None")

    for instruction in instructions:
        if instruction is None:
            raise ValueError("Instruction cannot be None")

        direction = parse_direction(instruction)
        distance = parse_distance(instruction)

        # 1) How many steps until we FIRST land on 0 going in this direction?
        if direction == "R":
            # From position p, going right:
            # positions: p+1, p+2, ..., p+d
            # next 0 is at k = 100 - p (if p > 0), or k = 100 (if p == 0)
            first_step_to_zero = 100 - position if position != 0 else 100
        else:  # direction == "L"
            # From position p, going left:
            # positions: p-1, p-2, ..., p-d
            # next 0 is at k = p (if p > 0), or k = 100 (if p == 0)
            first_step_to_zero = position if position != 0 else 100

        hits_this_instruction = 0

        # 2) If we don't get far enough to reach the first 0, no hits.
        if distance >= first_step_to_zero:
            # We hit 0 once at first_step_to_zero,
            # then every 100 clicks after that.
            remaining_after_first = distance - first_step_to_zero
            hits_this_instruction = 1 + (remaining_after_first // 100)

        zero_count += hits_this_instruction

        # 3) Update final position on the dial
        if direction == "R":
            position = (position + distance) % 100
        else:  # "L"
            position = (position - distance) % 100

    return zero_count


def main():
    with open("day_1_input.txt", "r") as file:
        instructions = [line.strip() for line in file.readlines()]

    zero_count = count_zero_positions(instructions)

    print(f"The lock landed on position 0 a total of {zero_count} times.")


if __name__ == "__main__":
    main()
