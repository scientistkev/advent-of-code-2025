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
    # Split each line by spaces and filter out empty strings
    # This creates a list of lists, where each inner list represents a row
    rows = []
    for line in lines:
        items = [item for item in line.split(" ") if item]
        rows.append(items)
    
    # Find the maximum number of columns (problems)
    max_cols = max(len(row) for row in rows) if rows else 0
    
    # The last row contains operations, all other rows contain numbers
    operations_row = rows[-1] if rows else []
    number_rows = rows[:-1] if len(rows) > 1 else []
    
    # Parse each column (problem)
    problems = []
    for col_idx in range(max_cols):
        # Collect numbers from all number rows for this column
        numbers = []
        for row in number_rows:
            if col_idx < len(row):
                try:
                    numbers.append(int(row[col_idx]))
                except ValueError:
                    # Skip if not a valid number
                    pass
        
        # Get operation from the operations row
        operation = operations_row[col_idx] if col_idx < len(operations_row) else None
        
        if numbers and operation:
            problems.append((numbers, operation))
    
    return problems


def solve_problems(problems):
    total = 0
    for numbers, operation in problems:
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


# PART 2: The big cephalopods come back to check on how things are going. When they see that your grand total doesn't match the one expected by the worksheet, they realize they forgot to explain how to read cephalopod math.

# Cephalopod math is written right-to-left in columns. Each number is given in its own column, with the most significant digit at the top and the least significant digit at the bottom. (Problems are still separated with a column consisting only of spaces, and the symbol at the bottom of the problem is still the operator to use.)

# Here's the example worksheet again:

# 123 328  51 64 
#  45 64  387 23 
#   6 98  215 314
# *   +   *   +  
# Reading the problems right-to-left one column at a time, the problems are now quite different:

# The rightmost problem is 4 + 431 + 623 = 1058
# The second problem from the right is 175 * 581 * 32 = 3253600
# The third problem from the right is 8 + 248 + 369 = 625
# Finally, the leftmost problem is 356 * 24 * 1 = 8544
# Now, the grand total is 1058 + 3253600 + 625 + 8544 = 3263827.

# Solve the problems on the math worksheet again. What is the grand total found by adding together all of the answers to the individual problems?

def parse_problems_right_to_left(lines):
    # Convert lines to a 2D grid of characters
    # Pad all lines to the same length
    max_len = max(len(line) for line in lines) if lines else 0
    grid = []
    for line in lines:
        padded_line = line.ljust(max_len)
        grid.append(list(padded_line))
    
    if not grid:
        return []
    
    num_rows = len(grid)
    num_cols = max_len
    
    # The last row contains operations
    operations_row = grid[-1]
    number_rows = grid[:-1]
    
    problems = []
    col = num_cols - 1  # Start from the rightmost column
    
    while col >= 0:
        # Skip columns that are all spaces (problem separators)
        if all(row[col] == ' ' for row in grid):
            col -= 1
            continue
        
        # Find the left boundary of this problem
        problem_start_col = col
        while problem_start_col >= 0:
            if all(row[problem_start_col] == ' ' for row in grid):
                problem_start_col += 1
                break
            problem_start_col -= 1
        if problem_start_col < 0:
            problem_start_col = 0
        
        # Parse numbers from right to left
        # Key insight: Each column represents one number
        # Within each column, digits are arranged top to bottom (MSD to LSD)
        # Read each column from top to bottom to get the digits, forming the number
        
        numbers = []
        current_col = col
        
        while current_col >= problem_start_col:
            # Skip if this column is all spaces
            if all(row[current_col] == ' ' for row in number_rows):
                current_col -= 1
                continue
            
            # Read this column from top to bottom to extract digits
            col_digits = []
            for row in number_rows:
                char = row[current_col]
                if char.isdigit():
                    col_digits.append(char)
            
            # If we found digits, form the number
            if col_digits:
                # Digits are read top to bottom, which gives MSD to LSD
                num_str = ''.join(col_digits)
                try:
                    numbers.append(int(num_str))
                except ValueError:
                    pass
            
            current_col -= 1
        
        # Get the operation for this problem (look in the operations row)
        operation = None
        for c in range(problem_start_col, col + 1):
            op_char = operations_row[c]
            if op_char in ('+', '*'):
                operation = op_char
                break
        
        if numbers and operation:
            # Numbers are collected right to left, which is the correct order
            problems.append((numbers, operation))
        
        col = problem_start_col - 1
    
    return problems


def solve_problems_right_to_left(problems):
    total = 0
    for numbers, operation in problems:
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
    problems = parse_problems_right_to_left(lines)
    grand_total = solve_problems_right_to_left(problems)
    print(f"Grand total of all problems: {grand_total}")


if __name__ == "__main__":
    main()