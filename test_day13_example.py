#!/usr/bin/env python3
import sys
sys.path.insert(0, 'challenges')
from day_13 import solve

# Example from problem statement
test_data = """0:
###
##.
##.

1:
###
##.
.##

2:
.##
###
##.

3:
##.
###
##.

4:
###
#..
###

5:
###
.#.
###

4x4: 0 0 0 0 2 0
12x5: 1 0 1 0 2 2
12x5: 1 0 1 0 3 2"""

print("Testing with example from problem statement...")
result = solve(test_data)
print(f"Result: {result} (expected: 2)")
