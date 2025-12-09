# The Elves are trying to figure out which junction boxes to connect so that electricity can reach every junction box. They even have a list of all of the junction boxes' positions in 3D space (your puzzle input).

# For example:

# 162,817,812
# 57,618,57
# 906,360,560
# 592,479,940
# 352,342,300
# 466,668,158
# 542,29,236
# 431,825,988
# 739,650,466
# 52,470,668
# 216,146,977
# 819,987,18
# 117,168,530
# 805,96,715
# 346,949,466
# 970,615,88
# 941,993,340
# 862,61,35
# 984,92,344
# 425,690,689
# This list describes the position of 20 junction boxes, one per line. Each position is given as X,Y,Z coordinates. So, the first junction box in the list is at X=162, Y=817, Z=812.

# To save on string lights, the Elves would like to focus on connecting pairs of junction boxes that are as close together as possible according to straight-line distance. In this example, the two junction boxes which are closest together are 162,817,812 and 425,690,689.

# By connecting these two junction boxes together, because electricity can flow between them, they become part of the same circuit. After connecting them, there is a single circuit which contains two junction boxes, and the remaining 18 junction boxes remain in their own individual circuits.

# Now, the two junction boxes which are closest together but aren't already directly connected are 162,817,812 and 431,825,988. After connecting them, since 162,817,812 is already connected to another junction box, there is now a single circuit which contains three junction boxes and an additional 17 circuits which contain one junction box each.

# The next two junction boxes to connect are 906,360,560 and 805,96,715. After connecting them, there is a circuit containing 3 junction boxes, a circuit containing 2 junction boxes, and 15 circuits which contain one junction box each.

# The next two junction boxes are 431,825,988 and 425,690,689. Because these two junction boxes were already in the same circuit, nothing happens!

# This process continues for a while, and the Elves are concerned that they don't have enough extension cables for all these circuits. They would like to know how big the circuits will be.

# After making the ten shortest connections, there are 11 circuits: one circuit which contains 5 junction boxes, one circuit which contains 4 junction boxes, two circuits which contain 2 junction boxes each, and seven circuits which each contain a single junction box. Multiplying together the sizes of the three largest circuits (5, 4, and one of the circuits of size 2) produces 40.

# Your list contains many junction boxes; connect together the 1000 pairs of junction boxes which are closest together. Afterward, what do you get if you multiply together the sizes of the three largest circuits?

def load_data(path):
    with open(path, "r") as f:
        return [line.rstrip("\n") for line in f.readlines()]

def parse_input(data):
    return [tuple(map(int, line.split(","))) for line in data]

def find_closest_pairs(boxes):
    closest_pairs = []
    for i in range(len(boxes)):
        for j in range(i + 1, len(boxes)):
            distance = sum(abs(a - b) for a, b in zip(boxes[i], boxes[j]))
            closest_pairs.append((i, j, distance))
    return closest_pairs

def find_largest_circuits(closest_pairs):
    closest_pairs.sort(key=lambda x: x[2])
    return closest_pairs[:1000]

def find_largest_circuits_size(closest_pairs):
    return len(closest_pairs)

def product_of_largest_circuits(largest_circuits):
    return product(largest_circuits)
def product(numbers):
    result = 1
    for number in numbers:
        result *= number
    return result

if __name__ == "__main__":
    data = load_data("data/day_9_input.txt")
    boxes = parse_input(data)
    closest_pairs = find_closest_pairs(boxes)
    largest_circuits = find_largest_circuits(closest_pairs)
    product = product_of_largest_circuits(largest_circuits)
    print(f"Product of the sizes of the three largest circuits: {product}")
    print(f"Largest circuits: {largest_circuits}")  
    print(f"Largest circuits size: {largest_circuits_size}")
 
