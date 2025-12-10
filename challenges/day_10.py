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
                area = abs(x2 - x1) * abs(y2 - y1)
                max_area = max(max_area, area)

    return max_area


def main():
    coordinates = load_data("data/day_10_input.txt")
    largest_area = find_largest_rectangle(coordinates)
    print(f"Largest rectangle area: {largest_area}")


if __name__ == "__main__":
    main()
