#!/usr/bin/env python3
import sys
sys.path.insert(0, 'challenges')
from day_13 import parse_shapes, parse_regions, get_all_variants, solve_region

# Simple test case
test_data = """0:
###
#..

4x4: 2 0"""

print("Testing parsing...")
shapes = parse_shapes(test_data)
print(f"Shapes: {shapes}")

regions = parse_regions(test_data)
print(f"Regions: {regions}")

if shapes and regions:
    width, length, counts = regions[0]
    print(f"\nTesting region {width}x{length} with counts {counts}")
    
    # Get variants
    shape_variants = {}
    for idx, shape in shapes.items():
        shape_variants[idx] = get_all_variants(shape)
        print(f"Shape {idx} has {len(shape_variants[idx])} variants")
    
    # Build shape_variants_list
    max_idx = len(counts) - 1
    shape_variants_list = []
    for i in range(max_idx + 1):
        if i in shape_variants:
            shape_variants_list.append(shape_variants[i])
        else:
            shape_variants_list.append([])
    
    print(f"\nTesting solve_region...")
    result = solve_region(width, length, shape_variants_list, counts)
    print(f"Result: {result}")
