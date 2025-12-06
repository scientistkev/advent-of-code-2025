# As you try to find a way out, you are approached by a family of cephalopods! They're pretty sure they can get the door open, but it will take some time. While you wait, they're curious if you can help the youngest cephalopod with her math homework.

# Cephalopod math doesn't look that different from normal math. The math worksheet (your puzzle input) consists of a list of problems; each problem has a group of numbers that need to be either added (+) or multiplied (*) together.

# However, the problems are arranged a little strangely; they seem to be presented next to each other in a very long horizontal list. For example:

# 123 328  51 64
#  45 64  387 23
#   6 98  215 314
# *   +   *   +
# Each problem's numbers are arranged vertically; at the bottom of the problem is the symbol for the operation that needs to be performed. Problems are separated by a full column of only spaces. The left/right alignment of numbers within each problem can be ignored.

# So, this worksheet contains four problems:

# 123 * 45 * 6 = 33210
# 328 + 64 + 98 = 490
# 51 * 387 * 215 = 4243455
# 64 + 23 + 314 = 401
# To check their work, cephalopod students are given the grand total of adding together all of the answers to the individual problems. In this worksheet, the grand total is 33210 + 490 + 4243455 + 401 = 4277556.

# Of course, the actual worksheet is much wider. You'll need to make sure to unroll it completely so that you can read the problems clearly.


def load_data(path):
    with open(path, "r") as f:
        lines = f.readlines()
    return [line.rstrip("\n") for line in lines]


def parse_problems(lines):
    return [line.split(" ") for line in lines]


def solve_problems(problems):
    total = 0
    for problem in problems:
        numbers = list(map(int, problem[:-1]))
        operation = problem[-1]
        if operation == "+":
            total += sum(numbers)
        elif operation == "*":
            product = 1
            for number in numbers:
                product *= number
            total += product
    return total


def main():
    lines = load_data("data/day_7_input.txt")
    problems = parse_problems(lines)
    grand_total = solve_problems(problems)
    print(f"Grand total of all problems: {grand_total}")


if __name__ == "__main__":
    main()
