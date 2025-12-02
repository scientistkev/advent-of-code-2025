# 1. Lock starts at position p
# 2. The lock can move a distance d
# 3. The lock can move in two directions: left (L) and right (R), -d or +d
# 3a. If there were no wraparound, p+d is the new position when moving right (R)
# 3b. If there were no wraparound, p-d is the new position when moving left (L)
# 4. The position changes with wraparound:
#   - If moving right and p+d > 99, the new position is (p + d) % 100
#   - If moving left and p-d < 0, the new position is (p - d) % 100
# 5. If the new position is 0, count it


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

    for instruction in instructions:
        direction = parse_direction(instruction)
        distance = parse_distance(instruction)
        movement = translate_direction_into_movement(direction, distance)

        position = (position + movement) % 100

        if position == 0:
            zero_count += 1

    return zero_count


def main():
    with open("day_1_input.txt", "r") as file:
        instructions = [line.strip() for line in file.readlines()]

    zero_count = count_zero_positions(instructions)
    print(f"The lock landed on position 0 a total of {zero_count} times.")


if __name__ == "__main__":
    main()
