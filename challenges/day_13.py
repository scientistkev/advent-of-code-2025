# --- Day 13: Christmas Tree Farm ---
# You're almost out of time, but there can't be much left to decorate. Although there are no stairs, elevators, escalators, tunnels, chutes, teleporters, firepoles, or conduits here that would take you deeper into the North Pole base, there is a ventilation duct. You jump in.

# After bumping around for a few minutes, you emerge into a large, well-lit cavern full of Christmas trees!

# There are a few Elves here frantically decorating before the deadline. They think they'll be able to finish most of the work, but the one thing they're worried about is the presents for all the young Elves that live here at the North Pole. It's an ancient tradition to put the presents under the trees, but the Elves are worried they won't fit.

# The presents come in a few standard but very weird shapes. The shapes and the regions into which they need to fit are all measured in standard units. To be aesthetically pleasing, the presents need to be placed into the regions in a way that follows a standardized two-dimensional unit grid; you also can't stack presents.

# As always, the Elves have a summary of the situation (your puzzle input) for you. First, it contains a list of the presents' shapes. Second, it contains the size of the region under each tree and a list of the number of presents of each shape that need to fit into that region. For example:

# 0:
# ###
# ##.
# ##.

# 1:
# ###
# ##.
# .##

# 2:
# .##
# ###
# ##.

# 3:
# ##.
# ###
# ##.

# 4:
# ###
# #..
# ###

# 5:
# ###
# .#.
# ###

# 4x4: 0 0 0 0 2 0
# 12x5: 1 0 1 0 2 2
# 12x5: 1 0 1 0 3 2
# The first section lists the standard present shapes. For convenience, each shape starts with its index and a colon; then, the shape is displayed visually, where # is part of the shape and . is not.

# The second section lists the regions under the trees. Each line starts with the width and length of the region; 12x5 means the region is 12 units wide and 5 units long. The rest of the line describes the presents that need to fit into that region by listing the quantity of each shape of present; 1 0 1 0 3 2 means you need to fit one present with shape index 0, no presents with shape index 1, one present with shape index 2, no presents with shape index 3, three presents with shape index 4, and two presents with shape index 5.

# Presents can be rotated and flipped as necessary to make them fit in the available space, but they have to always be placed perfectly on the grid. Shapes can't overlap (that is, the # part from two different presents can't go in the same place on the grid), but they can fit together (that is, the . part in a present's shape's diagram does not block another present from occupying that space on the grid).

# The Elves need to know how many of the regions can fit the presents listed. In the above example, there are six unique present shapes and three regions that need checking.

# The first region is 4x4:

# ....
# ....
# ....
# ....
# In it, you need to determine whether you could fit two presents that have shape index 4:

# ###
# #..
# ###
# After some experimentation, it turns out that you can fit both presents in this region. Here is one way to do it, using A to represent one present and B to represent the other:

# AAA.
# ABAB
# ABAB
# .BBB
# The second region, 12x5: 1 0 1 0 2 2, is 12 units wide and 5 units long. In that region, you need to try to fit one present with shape index 0, one present with shape index 2, two presents with shape index 4, and two presents with shape index 5.

# It turns out that these presents can all fit in this region. Here is one way to do it, again using different capital letters to represent all the required presents:

# ....AAAFFE.E
# .BBBAAFFFEEE
# DDDBAAFFCECE
# DBBB....CCC.
# DDD.....C.C.
# The third region, 12x5: 1 0 1 0 3 2, is the same size as the previous region; the only difference is that this region needs to fit one additional present with shape index 4. Unfortunately, no matter how hard you try, there is no way to fit all of the presents into this region.

# So, in this example, 2 regions can fit all of their listed presents.

# Consider the regions beneath each tree and the presents the Elves would like to fit into each of them. How many of the regions can fit all of the presents listed?

def load_data(path):
    with open(path, "r") as f:
        return f.read().strip()

def parse_shapes(data):
    """Parse present shapes from input."""
    shapes = {}
    lines = data.split('\n')
    i = 0
    while i < len(lines):
        line = lines[i].strip()
        if not line:
            i += 1
            continue
        # Check if this is a shape definition (e.g., "0:")
        if ':' in line and line.split(':')[0].strip().isdigit():
            shape_idx = int(line.split(':')[0].strip())
            shape_lines = []
            i += 1
            # Read shape lines until we hit a blank line or another shape/region definition
            while i < len(lines):
                next_line = lines[i].strip()
                if not next_line:
                    break
                # Check if next line is a new shape or region definition
                if ':' in next_line and (next_line.split(':')[0].strip().isdigit() or 'x' in next_line.split(':')[0]):
                    break
                if next_line and ('#' in next_line or '.' in next_line):
                    shape_lines.append(next_line)
                    i += 1
                else:
                    break
            if shape_lines:
                shapes[shape_idx] = shape_lines
        else:
            i += 1
    return shapes

def parse_regions(data):
    """Parse region requirements from input."""
    regions = []
    lines = data.split('\n')
    for line in lines:
        line = line.strip()
        if not line:
            continue
        # Check if this is a region definition (e.g., "12x5: 1 0 1 0 2 2")
        if 'x' in line and ':' in line:
            parts = line.split(':')
            dims = parts[0].strip()
            counts_str = parts[1].strip()
            width, length = map(int, dims.split('x'))
            counts = list(map(int, counts_str.split()))
            regions.append((width, length, counts))
    return regions

def rotate_shape(shape):
    """Rotate shape 90 degrees clockwise."""
    if not shape:
        return []
    rows = len(shape)
    cols = len(shape[0])
    rotated = []
    for c in range(cols):
        new_row = ''.join(shape[r][c] for r in range(rows - 1, -1, -1))
        rotated.append(new_row)
    return rotated

def flip_shape(shape):
    """Flip shape horizontally."""
    return [row[::-1] for row in shape]

def get_all_variants(shape):
    """Get all rotations and flips of a shape."""
    variants = set()
    
    # Generate all 4 rotations
    current = shape
    for _ in range(4):
        # Convert to tuple for hashing
        variant_tuple = tuple(current)
        variants.add(variant_tuple)
        current = rotate_shape(current)
    
    # Generate all 4 rotations of flipped version
    flipped = flip_shape(shape)
    current = flipped
    for _ in range(4):
        variant_tuple = tuple(current)
        variants.add(variant_tuple)
        current = rotate_shape(current)
    
    return [list(v) for v in variants]

def get_shape_cells(shape, row_offset, col_offset):
    """Get set of (row, col) positions occupied by shape when placed at offset."""
    cells = set()
    for r, row in enumerate(shape):
        for c, char in enumerate(row):
            if char == '#':
                cells.add((row_offset + r, col_offset + c))
    return cells

def can_place_shape(grid, shape, row, col, width, length):
    """Check if shape can be placed at (row, col) position."""
    shape_rows = len(shape)
    shape_cols = len(shape[0])
    
    # Check bounds
    if row + shape_rows > length or col + shape_cols > width:
        return False
    
    # Check if shape cells overlap with already occupied cells
    for r in range(shape_rows):
        for c in range(shape_cols):
            if shape[r][c] == '#':
                if grid[row + r][col + c] != '.':
                    return False
    
    return True

def place_shape(grid, shape, row, col, shape_id):
    """Place shape on grid at (row, col) position."""
    shape_rows = len(shape)
    shape_cols = len(shape[0])
    
    for r in range(shape_rows):
        for c in range(shape_cols):
            if shape[r][c] == '#':
                grid[row + r][col + c] = shape_id

def remove_shape(grid, shape, row, col):
    """Remove shape from grid at (row, col) position."""
    shape_rows = len(shape)
    shape_cols = len(shape[0])
    
    for r in range(shape_rows):
        for c in range(shape_cols):
            if shape[r][c] == '#':
                grid[row + r][col + c] = '.'

def solve_region(width, length, shape_variants_list, required_counts):
    """Try to fit all required shapes into a region using backtracking."""
    # Create grid (length x width)
    grid = [['.' for _ in range(width)] for _ in range(length)]
    
    # Flatten shape variants and required counts into a list of shapes to place
    shapes_to_place = []
    for shape_idx, count in enumerate(required_counts):
        for _ in range(count):
            shapes_to_place.append((shape_idx, shape_variants_list[shape_idx]))
    
    if not shapes_to_place:
        return True
    
    def backtrack(shape_idx):
        if shape_idx >= len(shapes_to_place):
            return True
        
        shape_type, variants = shapes_to_place[shape_idx]
        
        # Try each variant of this shape
        for variant in variants:
            # Try placing at each position
            for row in range(length):
                for col in range(width):
                    if can_place_shape(grid, variant, row, col, width, length):
                        # Place the shape
                        place_shape(grid, variant, row, col, shape_type)
                        
                        # Recursively try to place remaining shapes
                        if backtrack(shape_idx + 1):
                            return True
                        
                        # Backtrack: remove the shape
                        remove_shape(grid, variant, row, col)
        
        return False
    
    return backtrack(0)

def solve(data):
    """Main solving function."""
    # Parse shapes and regions
    shapes = parse_shapes(data)
    regions = parse_regions(data)
    
    # Generate all variants for each shape
    shape_variants = {}
    for shape_idx, shape in shapes.items():
        shape_variants[shape_idx] = get_all_variants(shape)
    
    # Count how many regions can fit all their presents
    count = 0
    for width, length, required_counts in regions:
        # Get variants for shapes that are needed
        max_shape_idx = len(required_counts) - 1
        shape_variants_list = []
        for i in range(max_shape_idx + 1):
            if i in shape_variants:
                shape_variants_list.append(shape_variants[i])
            else:
                shape_variants_list.append([])
        
        if solve_region(width, length, shape_variants_list, required_counts):
            count += 1
    
    return count

if __name__ == "__main__":
    data = load_data("data/day_13_input.txt")
    result = solve(data)
    print(f"Number of regions that can fit all their presents: {result}")
