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
            # Calculate squared Euclidean distance for comparison (avoids floating point issues)
            # Using squared distance preserves ordering and is faster
            distance_sq = sum((a - b) ** 2 for a, b in zip(boxes[i], boxes[j]))
            closest_pairs.append((i, j, distance_sq))
    return closest_pairs

class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
        self.size = [1] * n
    
    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]
    
    def union(self, x, y):
        root_x = self.find(x)
        root_y = self.find(y)
        if root_x != root_y:
            if self.size[root_x] < self.size[root_y]:
                root_x, root_y = root_y, root_x
            self.parent[root_y] = root_x
            self.size[root_x] += self.size[root_y]

def connect_circuits(boxes, num_connections=1000):
    closest_pairs = find_closest_pairs(boxes)
    # Sort by distance, then by i, then by j for consistent ordering of ties
    closest_pairs.sort(key=lambda x: (x[2], x[0], x[1]))
    
    uf = UnionFind(len(boxes))
    
    # Process exactly num_connections pairs (even if they don't result in a merge)
    for i, j, distance in closest_pairs[:num_connections]:
        if uf.find(i) != uf.find(j):
            uf.union(i, j)
    
    # Count circuit sizes by finding the root of each box and counting
    circuit_sizes = {}
    for i in range(len(boxes)):
        root = uf.find(i)
        circuit_sizes[root] = circuit_sizes.get(root, 0) + 1
    
    return list(circuit_sizes.values())

def product_of_largest_circuits(circuit_sizes, n=3):
    sorted_sizes = sorted(circuit_sizes, reverse=True)
    largest_n = sorted_sizes[:n]
    result = 1
    for size in largest_n:
        result *= size
    return result

if __name__ == "__main__":
    data = load_data("data/day_9_input.txt")
    boxes = parse_input(data)
    circuit_sizes = connect_circuits(boxes, num_connections=1000)
    product = product_of_largest_circuits(circuit_sizes, n=3)
    print(f"Product of the sizes of the three largest circuits: {product}")
 
