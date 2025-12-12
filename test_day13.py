#!/usr/bin/env python3
import sys
sys.path.insert(0, 'challenges')
from day_13 import solve, parse_shapes, parse_regions, get_all_variants

# Test with example data
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

print("Testing parsing...")
shapes = parse_shapes(test_data)
print(f"Parsed {len(shapes)} shapes: {list(shapes.keys())}")
for idx, shape in shapes.items():
    print(f"Shape {idx}: {len(shape)} rows")

regions = parse_regions(test_data)
print(f"\nParsed {len(regions)} regions:")
for width, length, counts in regions:
    print(f"  {width}x{length}: {counts}")

print("\nTesting variants...")
for idx, shape in shapes.items():
    variants = get_all_variants(shape)
    print(f"Shape {idx} has {len(variants)} variants")

print("\nTesting solve...")
result = solve(test_data)
print(f"Result: {result} (expected: 2)")
