# You slide down the firepole in the corner of the playground and land in the North Pole base movie theater!

# The movie theater has a big tile floor with an interesting pattern. Elves here are redecorating the theater by switching out some of the square tiles in the big grid they form. Some of the tiles are red; the Elves would like to find the largest rectangle that uses red tiles for two of its opposite corners. They even have a list of where the red tiles are located in the grid (your puzzle input).

# For example:

# 7,1
# 11,1
# 11,7
# 9,7
# 9,5
# 2,5
# 2,3
# 7,3
# Showing red tiles as # and other tiles as ., the above arrangement of red tiles would look like this:

# ..............
# .......#...#..
# ..............
# ..#....#......
# ..............
# ..#......#....
# ..............
# .........#.#..
# ..............
# You can choose any two red tiles as the opposite corners of your rectangle; your goal is to find the largest rectangle possible.

# For example, you could make a rectangle (shown as O) with an area of 24 between 2,5 and 9,7:

# ..............
# .......#...#..
# ..............
# ..#....#......
# ..............
# ..OOOOOOOO....
# ..OOOOOOOO....
# ..OOOOOOOO.#..
# ..............
# Or, you could make a rectangle with area 35 between 7,1 and 11,7:

# ..............
# .......OOOOO..
# .......OOOOO..
# ..#....OOOOO..
# .......OOOOO..
# ..#....OOOOO..
# .......OOOOO..
# .......OOOOO..
# ..............
# You could even make a thin rectangle with an area of only 6 between 7,3 and 2,3:

# ..............
# .......#...#..
# ..............
# ..OOOOOO......
# ..............
# ..#......#....
# ..............
# .........#.#..
# ..............
# Ultimately, the largest rectangle you can make in this example has area 50. One way to do this is between 2,5 and 11,1:

# ..............
# ..OOOOOOOOOO..
# ..OOOOOOOOOO..
# ..OOOOOOOOOO..
# ..OOOOOOOOOO..
# ..OOOOOOOOOO..
# ..............
# .........#.#..
# ..............
# Using two red tiles as opposite corners, what is the largest area of any rectangle you can make?


def load_data(path):
    with open(path, "r") as f:
        lines = f.readlines()
    coordinates = []
    for line in lines:
        x, y = map(int, line.strip().split(","))
        coordinates.append((x, y))
    return coordinates


def find_largest_rectangle(coordinates):
    max_area = 0
    n = len(coordinates)

    for i in range(n):
        x1, y1 = coordinates[i]
        for j in range(i + 1, n):
            x2, y2 = coordinates[j]
            # Two points form opposite corners if they have different x and y coordinates
            if x1 != x2 and y1 != y2:
                # Area calculation: width * height, where both are inclusive
                # If corners are at x1 and x2, the width is |x2-x1|+1 (inclusive)
                area = (abs(x2 - x1) + 1) * (abs(y2 - y1) + 1)
                max_area = max(max_area, area)

    return max_area


# The Elves just remembered: they can only switch out tiles that are red or green. So, your rectangle can only include red or green tiles.

# In your list, every red tile is connected to the red tile before and after it by a straight line of green tiles. The list wraps, so the first red tile is also connected to the last red tile. Tiles that are adjacent in your list will always be on either the same row or the same column.

# Using the same example as before, the tiles marked X would be green:

# ..............
# .......#XXX#..
# .......X...X..
# ..#XXXX#...X..
# ..X........X..
# ..#XXXXXX#.X..
# .........X.X..
# .........#X#..
# ..............
# In addition, all of the tiles inside this loop of red and green tiles are also green. So, in this example, these are the green tiles:

# ..............
# .......#XXX#..
# .......XXXXX..
# ..#XXXX#XXXX..
# ..XXXXXXXXXX..
# ..#XXXXXX#XX..
# .........XXX..
# .........#X#..
# ..............
# The remaining tiles are never red nor green.

# The rectangle you choose still must have red tiles in opposite corners, but any other tiles it includes must now be red or green. This significantly limits your options.

# For example, you could make a rectangle out of red and green tiles with an area of 15 between 7,3 and 11,1:

# ..............
# .......OOOOO..
# .......OOOOO..
# ..#XXXXOOOOO..
# ..XXXXXXXXXX..
# ..#XXXXXX#XX..
# .........XXX..
# .........#X#..
# ..............
# Or, you could make a thin rectangle with an area of 3 between 9,7 and 9,5:

# ..............
# .......#XXX#..
# .......XXXXX..
# ..#XXXX#XXXX..
# ..XXXXXXXXXX..
# ..#XXXXXXOXX..
# .........OXX..
# .........OX#..
# ..............
# The largest rectangle you can make in this example using only red and green tiles has area 24. One way to do this is between 9,5 and 2,3:

# ..............
# .......#XXX#..
# .......XXXXX..
# ..OOOOOOOOXX..
# ..OOOOOOOOXX..
# ..OOOOOOOOXX..
# .........XXX..
# .........#X#..
# ..............
# # Using two red tiles as opposite corners, what is the largest area of any rectangle you can make using only red and green tiles?

def get_sign(num):
    """Return the sign of a number: 1 for positive, -1 for negative, 0 for zero."""
    if num > 0:
        return 1
    elif num < 0:
        return -1
    else:
        return 0


def check_point_in_shape(shape, point):
    """
    Check if a point is inside the shape using ray casting algorithm.
    A horizontal ray is drawn from the point to the left edge.
    Odd number of intersections means the point is inside the shape.
    This function is for points whose coordinates are not integers (adjusted by 0.5).
    """
    px, py = point
    intersections = 0
    
    for index, vertex in enumerate(shape):
        prev_vertex = shape[index - 1]
        vx, vy = vertex
        pvx, pvy = prev_vertex
        
        # Check if this edge is a vertical line to the left of the point
        if vx == pvx and vx < px:
            # Check if the point's y-coordinate is between the edge's y-coordinates
            if (vy < py < pvy) or (vy > py > pvy):
                intersections += 1
    
    return intersections % 2 == 1


def check_segment_no_intersection(shape, point_a, point_b):
    """
    Check if a segment (between point_a and point_b) doesn't intersect
    the shape boundary. Returns True if no intersection, False otherwise.
    """
    ax, ay = point_a
    bx, by = point_b
    
    if ay == by:  # Horizontal segment
        for index, vertex in enumerate(shape):
            prev_vertex = shape[index - 1]
            vx, vy = vertex
            pvx, pvy = prev_vertex
            
            # Check if this edge is a vertical line that intersects the horizontal segment
            if vx == pvx:  # Vertical edge
                if min(ax, bx) < vx < max(ax, bx):  # Edge x is within segment x range
                    if min(vy, pvy) < ay < max(vy, pvy):  # Segment y is within edge y range
                        return False
    
    elif ax == bx:  # Vertical segment
        for index, vertex in enumerate(shape):
            prev_vertex = shape[index - 1]
            vx, vy = vertex
            pvx, pvy = prev_vertex
            
            # Check if this edge is a horizontal line that intersects the vertical segment
            if vy == pvy:  # Horizontal edge
                if min(ay, by) < vy < max(ay, by):  # Edge y is within segment y range
                    if min(vx, pvx) < ax < max(vx, pvx):  # Segment x is within edge x range
                        return False
    
    return True


def find_largest_rectangle_with_green(coordinates):
    """
    Find the largest rectangle (in number of tiles) that:
      - Has red tiles at opposite corners
      - Contains only red or green tiles in its area
    
    Uses point-in-polygon testing to efficiently check if rectangles are valid.
    """
    if not coordinates:
        return 0
    
    red_tiles = set(coordinates)
    max_area = 0
    n = len(coordinates)
    
    # Generate all candidate pairs and sort by area (descending) for early pruning
    pairs = []
    for i in range(n):
        x1, y1 = coordinates[i]
        for j in range(i + 1, n):
            x2, y2 = coordinates[j]
            if x1 != x2 and y1 != y2:
                area = (abs(x2 - x1) + 1) * (abs(y2 - y1) + 1)
                pairs.append((area, x1, y1, x2, y2))
    
    pairs.sort(reverse=True)
    
    for area, x1, y1, x2, y2 in pairs:
        # Early pruning: if this area can't beat current max, skip
        if area <= max_area:
            break
        
        # Verify both corners are red tiles
        if (x1, y1) not in red_tiles or (x2, y2) not in red_tiles:
            continue
        
        # Adjust corners by 0.5 to avoid edge cases where corners might be exactly on boundary
        x_diff = x1 - x2
        y_diff = y1 - y2
        
        adjusted_a0 = x1 - 0.5 * get_sign(x_diff)
        adjusted_a1 = y1 - 0.5 * get_sign(y_diff)
        adjusted_b0 = x2 + 0.5 * get_sign(x_diff)
        adjusted_b1 = y2 + 0.5 * get_sign(y_diff)
        
        # Four corners of the rectangle (adjusted)
        points = [
            (adjusted_a0, adjusted_a1),
            (adjusted_a0, adjusted_b1),
            (adjusted_b0, adjusted_b1),
            (adjusted_b0, adjusted_a1),
        ]
        
        # Check if all four corners are inside the shape
        points_check_passed = True
        for j, point in enumerate(points):
            if not check_point_in_shape(coordinates, point):
                points_check_passed = False
                break
            # Check if the edge from this point to the previous point doesn't intersect
            if not check_segment_no_intersection(coordinates, point, points[j - 1]):
                points_check_passed = False
                break
        
        if points_check_passed:
            max_area = area
    
    return max_area


def main():
    coordinates = load_data("data/day_10_input.txt")
    
    # Part 1
    largest_area = find_largest_rectangle(coordinates)
    print(f"Largest rectangle area: {largest_area}")
    
    # Part 2
    largest_area_with_green = find_largest_rectangle_with_green(coordinates)
    print(f"Largest rectangle area using only red and green tiles: {largest_area_with_green}")


if __name__ == "__main__":
    main()
