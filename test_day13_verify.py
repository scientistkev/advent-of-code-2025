#!/usr/bin/env python3
# Test with the example from the problem statement

lines = """0:
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
12x5: 1 0 1 0 3 2""".split('\n')

in_shapes = True
shapes = {}
cur_shape_index = None
trees = []

for line in lines:
    line = line.strip()
    if in_shapes:
        if cur_shape_index is None:
            if line == '':
                continue
            cur_shape_index = int(line[:line.index(':')])
            shapes[cur_shape_index] = []
        else:
            shapes[cur_shape_index].append(tuple(line))
            
            if len(shapes[cur_shape_index]) == 3:
                cur_shape_index = None
                
                if len(shapes) == 6:
                    in_shapes = False
    else:
        if line == '':
            continue

        sp = line.split(':')
        size = tuple(map(int, sp[0].split('x')))
        counts = tuple(map(int, sp[1].strip().split()))

        trees.append((size, counts))

# Calculate area (number of '#' cells) for each shape
areas = [None] * len(shapes)
for k, v in shapes.items():
    total = 0
    for r in v:
        total += r.count('#')
    areas[k] = total
    print(f"Shape {k} area: {areas[k]}")

can_fit = 0
for size, counts in trees:
    total_size = size[0] * size[1]
    total_area = 0
    for ind, count in enumerate(counts):
        total_area += areas[ind] * count
    
    print(f"\nRegion {size[0]}x{size[1]}, counts: {counts}")
    print(f"  Total size: {total_size}, Total area needed: {total_area}")
    print(f"  (total_size // 9) = {total_size // 9}, sum(counts) = {sum(counts)}")
    
    if (total_size // 9) >= sum(counts):
        print(f"  -> FITS (heuristic)")
        can_fit += 1
    elif total_size < total_area:
        print(f"  -> DOESN'T FIT (area check)")
        continue
    else:
        print(f"  -> FITS (else case)")
        can_fit += 1

print(f"\nTotal regions that fit: {can_fit} (expected: 2)")
