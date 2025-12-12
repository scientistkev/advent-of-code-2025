# Test Part 2 with the example from the problem description

def parse_input(data):
    """Parse input data into a graph dictionary."""
    graph = {}
    for line in data:
        if ": " not in line:
            continue
        device, outputs_str = line.split(": ", 1)
        outputs = outputs_str.split()
        graph[device] = outputs
    return graph

def find_all_paths(graph, start, end, path=None):
    """Find all paths from start to end using DFS."""
    if path is None:
        path = []
    
    path = path + [start]
    
    # If we've reached the end, return this path
    if start == end:
        return [path]
    
    # If start is not in graph, no paths exist
    if start not in graph:
        return []
    
    paths = []
    # Explore all neighbors
    for neighbor in graph[start]:
        if neighbor not in path:  # Avoid cycles
            new_paths = find_all_paths(graph, neighbor, end, path)
            paths.extend(new_paths)
    
    return paths

def count_paths_with_required_nodes(data, start, end, required_nodes):
    """Count all paths from start to end that visit all required nodes."""
    graph = parse_input(data)
    all_paths = find_all_paths(graph, start, end)
    
    # Filter paths that contain all required nodes
    valid_paths = []
    for path in all_paths:
        if all(node in path for node in required_nodes):
            valid_paths.append(path)
    
    return len(valid_paths)

# Example from Part 2
example_data = [
    "svr: aaa bbb",
    "aaa: fft",
    "fft: ccc",
    "bbb: tty",
    "tty: ccc",
    "ccc: ddd eee",
    "ddd: hub",
    "hub: fff",
    "eee: dac",
    "dac: fff",
    "fff: ggg hhh",
    "ggg: out",
    "hhh: out"
]

result = count_paths_with_required_nodes(example_data, "svr", "out", ["dac", "fft"])
print(f"Example result: {result} (expected: 2)")

# Show all paths from svr to out
graph = parse_input(example_data)
all_paths = find_all_paths(graph, "svr", "out")
print(f"\nAll paths from svr to out ({len(all_paths)} total):")
for i, path in enumerate(all_paths, 1):
    print(f"  {i}: {' -> '.join(path)}")

print(f"\nPaths that visit both dac and fft:")
for i, path in enumerate(all_paths, 1):
    if "dac" in path and "fft" in path:
        print(f"  {i}: {' -> '.join(path)}")
