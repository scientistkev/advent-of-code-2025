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


def main():
    coordinates = load_data("data/day_10_input.txt")
    largest_area = find_largest_rectangle(coordinates)
    print(f"Largest rectangle area: {largest_area}")


if __name__ == "__main__":
    main()


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

def point_in_polygon(x, y, polygon):
    """Check if a point is inside a polygon using the ray casting algorithm."""
    n = len(polygon)
    inside = False

    p1x, p1y = polygon[0]
    for i in range(1, n + 1):
        p2x, p2y = polygon[i % n]

        if p1y != p2y:
            if min(p1y, p2y) < y <= max(p1y, p2y):
                if p1x == p2x:
                    if x < p1x:
                        inside = not inside
                else:
                    xinters = (y - p1y) * (p2x - p1x) / (p2y - p1y) + p1x
                    if x < xinters:
                        inside = not inside

        p1x, p1y = p2x, p2y

    return inside


def get_connecting_line_tiles(coordinates):
    """Pre-compute all tiles on lines connecting consecutive red tiles."""
    line_tiles = set()
    n = len(coordinates)

    for i in range(n):
        x1, y1 = coordinates[i]
        x2, y2 = coordinates[(i + 1) % n]

        # Tiles on the same row
        if y1 == y2:
            start_x, end_x = min(x1, x2), max(x1, x2)
            for x in range(start_x, end_x + 1):
                line_tiles.add((x, y1))
        # Tiles on the same column
        elif x1 == x2:
            start_y, end_y = min(y1, y2), max(y1, y2)
            for y in range(start_y, end_y + 1):
                line_tiles.add((x1, y))

    return line_tiles


def build_allowed_grid(coordinates):
    """
    Build a grid of allowed tiles (red or green) and a 2D prefix sum over that grid.

    Returns:
        allowed (list[list[bool]]): allowed[y][x] (after offset) is True if tile is red/green.
        prefix (list[list[int]]): 2D prefix sums over allowed grid.
        red_tiles (set[tuple[int,int]]): set of red tile coordinates.
        min_x, min_y (int): offsets used for grid coordinates.
    """
    red_tiles = set(coordinates)
    line_tiles = get_connecting_line_tiles(coordinates)

    xs = [x for x, _ in coordinates]
    ys = [y for _, y in coordinates]
    min_x, max_x = min(xs), max(xs)
    min_y, max_y = min(ys), max(ys)

    width = max_x - min_x + 1
    height = max_y - min_y + 1

    # Build allowed grid: True if red, on boundary line, or strictly inside polygon
    allowed = [[False] * width for _ in range(height)]

    for y in range(min_y, max_y + 1):
        row_idx = y - min_y
        for x in range(min_x, max_x + 1):
            col_idx = x - min_x
            pt = (x, y)

            if pt in red_tiles or pt in line_tiles or point_in_polygon(x, y, coordinates):
                allowed[row_idx][col_idx] = True

    # Build 2D prefix sums over allowed
    # prefix[ry+1][rx+1] = number of allowed tiles in [0..ry][0..rx]
    prefix = [[0] * (width + 1) for _ in range(height + 1)]
    for ry in range(height):
        row_sum = 0
        for rx in range(width):
            if allowed[ry][rx]:
                row_sum += 1
            prefix[ry + 1][rx + 1] = prefix[ry][rx + 1] + row_sum

    return allowed, prefix, red_tiles, min_x, min_y


def rect_allowed_count(prefix, x1, y1, x2, y2, min_x, min_y):
    """
    Return number of allowed tiles in rectangle [x1..x2] x [y1..y2] inclusive,
    using 2D prefix sums and coordinate offsets.
    """
    if x1 > x2:
        x1, x2 = x2, x1
    if y1 > y2:
        y1, y2 = y2, y1

    # Convert to grid indices
    gx1 = x1 - min_x
    gx2 = x2 - min_x
    gy1 = y1 - min_y
    gy2 = y2 - min_y

    # Standard 2D prefix sum query
    # Note prefix indices are 1-based relative to allowed indices
    total = (
        prefix[gy2 + 1][gx2 + 1]
        - prefix[gy1][gx2 + 1]
        - prefix[gy2 + 1][gx1]
        + prefix[gy1][gx1]
    )
    return total


def find_largest_rectangle_with_green(coordinates):
    """
    Find the largest rectangle with red tiles as opposite corners,
    using only red and green tiles inside (including boundary).
    """
    if not coordinates:
        return 0

    allowed, prefix, red_tiles, min_x, min_y = build_allowed_grid(coordinates)

    max_area = 0
    n = len(coordinates)

    # Precompute all candidate red-tile pairs with their potential areas
    pairs = []
    for i in range(n):
        x1, y1 = coordinates[i]
        for j in range(i + 1, n):
            x2, y2 = coordinates[j]

            # Opposite corners of an axis-aligned rectangle only
            if x1 != x2 and y1 != y2:
                area = (abs(x2 - x1) + 1) * (abs(y2 - y1) + 1)
                pairs.append((area, x1, y1, x2, y2))

    # Sort by area descending to check larger rectangles first
    pairs.sort(reverse=True)

    for area, x1, y1, x2, y2 in pairs:
        # Skip if this area can't beat current max
        if area <= max_area:
            break

        # All tiles in the rectangle must be allowed
        allowed_count = rect_allowed_count(prefix, x1, y1, x2, y2, min_x, min_y)
        if allowed_count == area:
            max_area = area

    return max_area


def main():
    coordinates = load_data("data/day_10_input.txt")

    # Part 1 (if you have this implemented elsewhere)
    try:
        largest_area = find_largest_rectangle(coordinates)
        print(f"Largest rectangle area: {largest_area}")
    except NameError:
        # Part 1 not defined in this file; skip it.
        pass

    # Part 2
    largest_area_with_green = find_largest_rectangle_with_green(coordinates)
    print(
        "Largest rectangle area using only red and green tiles: "
        f"{largest_area_with_green}"
    )


if __name__ == "__main__":
    main()