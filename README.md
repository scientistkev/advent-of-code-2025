# Advent of Code 2025

This repository contains my solutions to the [Advent of Code 2025](https://adventofcode.com/2025) programming challenges.

## What is Advent of Code?

Advent of Code is an annual programming competition that runs from December 1st through December 25th. Each day, participants receive a two-part programming puzzle that can be solved using any programming language. The puzzles are designed to be solved in about 30 minutes each, though they can range from straightforward to quite challenging. The event encourages problem-solving, algorithmic thinking, and creative solutions while building a festive coding tradition.

## Repository Structure

```
advent-of-code-2025/
├── challenges/          # Solution files for each day
│   ├── day_1.py
│   ├── day_2.py
│   ├── day_3.py
│   ├── day_4.py
│   ├── day_5.py
│   ├── day_6.py
│   ├── day_7.py
│   ├── day_8.py
│   ├── day_9.py
│   ├── day_10.py
│   ├── day_11.py
│   ├── day_12.py
│   └── day_13.py
├── data/               # Input files for each day
│   ├── day_1_input.txt
│   ├── day_2_input.txt
│   ├── day_4_input.txt
│   ├── day_5_input.txt
│   ├── day_6_input.txt
│   ├── day_7_input.txt
│   ├── day_8_input.txt
│   ├── day_9_input.txt
│   ├── day_10_input.txt
│   ├── day_11_input.txt
│   ├── day_12_input.txt
│   └── day_13_input.txt
├── tests/              # Test files
├── venv/               # Python virtual environment
├── LICENSE
└── README.md
```

## Problem Descriptions and Lessons Learned

### Day 1: Lock Position Tracking

**Problem**: Track a lock dial's position as it moves left and right based on instructions, counting how many times it lands on position 0.

**Lessons Learned**:

- Modular arithmetic is essential for handling wraparound scenarios
- Part 2 required careful tracking of intermediate positions during movement, not just final positions
- Understanding the problem statement precisely is crucial - counting "passes through" zero is different from counting "lands on" zero

### Day 2: Invalid Product ID Detection

**Problem**: Find product IDs that are invalid based on repeating digit patterns within ID ranges.

**Lessons Learned**:

- String manipulation and pattern matching are fundamental skills
- Part 2 expanded the pattern matching to detect any repeated subsequence, requiring careful analysis of string properties
- Efficiently checking for repeating patterns requires understanding divisibility properties

### Day 3: Range Overlap Detection

**Problem**: Determine which ingredient IDs are fresh based on overlapping ranges, then count total fresh IDs across merged ranges.

**Lessons Learned**:

- Range merging algorithms are useful for simplifying overlapping intervals
- Sorting ranges before merging makes the algorithm straightforward
- Part 2 required understanding set union operations on intervals

### Day 4: Optimal Joltage Selection

**Problem**: Find the maximum two-digit number formable from digits in order, then extend to finding the maximum 12-digit number.

**Lessons Learned**:

- Greedy algorithms work well for selecting optimal subsequences
- The key insight is maintaining a sliding window that ensures enough digits remain for the remaining positions
- Part 2 required careful tracking of remaining positions while maximizing each digit choice

### Day 5: Paper Roll Accessibility

**Problem**: Count paper rolls accessible by forklifts (those with fewer than 4 adjacent rolls), then simulate iterative removal.

**Lessons Learned**:

- Grid-based problems often require careful boundary checking
- Part 2 introduced an iterative process where removing items creates new accessible items
- Understanding when to use iterative vs. recursive approaches matters for efficiency

### Day 6: Fresh Ingredient Range Analysis

**Problem**: Check which ingredient IDs fall within fresh ranges, then count total unique IDs across all ranges.

**Lessons Learned**:

- Simple range membership checking is straightforward but can be optimized
- Merging overlapping ranges reduces redundant checks
- Set operations can simplify counting unique values across ranges

### Day 7: Cephalopod Math

**Problem**: Parse vertically arranged math problems and solve them, accounting for right-to-left reading order in part 2.

**Lessons Learned**:

- Parsing non-standard formats requires careful attention to alignment and spacing
- Part 2's right-to-left reading fundamentally changed the problem structure
- Column-based parsing requires understanding how data is organized spatially

### Day 8: Tachyon Beam Splitting

**Problem**: Simulate tachyon beams splitting at splitters, counting total splits, then count all possible quantum timelines.

**Lessons Learned**:

- Simulation problems require careful state tracking
- Part 2's quantum interpretation required dynamic programming/memoization to avoid exponential explosion
- Understanding the problem's interpretation (classical vs. quantum) fundamentally changes the approach

### Day 9: Junction Box Circuit Connection

**Problem**: Connect closest junction boxes using Union-Find, then find the connection that completes the circuit.

**Lessons Learned**:

- Union-Find (Disjoint Set Union) is essential for connectivity problems
- Part 2 required continuing until all nodes are connected, demonstrating the power of Union-Find for minimum spanning tree-like problems
- Efficient distance calculations using squared distances avoid floating-point precision issues

### Day 10: Largest Rectangle Finding

**Problem**: Find the largest rectangle with red tiles at opposite corners, then restrict to rectangles containing only red/green tiles.

**Lessons Learned**:

- Geometric problems often require point-in-polygon algorithms
- Part 2 introduced complex constraints requiring ray-casting algorithms
- Understanding coordinate systems and boundary conditions is critical for geometric problems

### Day 11: Machine Button Configuration

**Problem**: Find minimum button presses to configure indicator lights, then configure joltage counters using linear programming.

**Lessons Learned**:

- Part 1 was solvable with brute force (each button pressed 0 or 1 times)
- Part 2 required integer linear programming (ILP) for efficiency
- Using libraries like PuLP demonstrates when to leverage existing tools vs. implementing from scratch

### Day 12: Path Counting in Directed Graph

**Problem**: Count all paths from "you" to "out", then count paths visiting specific nodes in order.

**Lessons Learned**:

- Topological sorting enables efficient path counting using dynamic programming
- Part 2 required breaking paths into segments and multiplying path counts
- Understanding graph properties (DAG) enables optimization techniques

### Day 13: Present Fitting Puzzle

**Problem**: Determine if presents of various shapes can fit into regions under Christmas trees.

**Lessons Learned**:

- This is a complex packing problem that would typically require backtracking
- Heuristic approaches can work when full solutions are computationally expensive
- Area-based checks provide quick filtering before attempting full solutions

## How to Obtain the Solutions

### Prerequisites

- Python 3.x
- (Optional) PuLP library for Day 11 Part 2: `pip install pulp`

### Running Solutions

Each day's solution is in the `challenges/` directory. To run a solution:

1. Navigate to the repository directory:

   ```bash
   cd advent-of-code-2025
   ```

2. Run the desired day's solution:

   ```bash
   python challenges/day_X.py
   ```

   Replace `X` with the day number (1-13).

3. **Note**: Input files are expected to be in the `data/` directory. The solutions reference input files using relative paths like `data/day_X_input.txt`.

### Getting Your Own Input Files

To solve these problems yourself:

1. Visit [Advent of Code 2025](https://adventofcode.com/2025)
2. Log in with your account (or create one)
3. Navigate to the specific day's problem
4. Download your personalized input file
5. Save it in the `data/` directory with the appropriate filename (e.g., `day_1_input.txt`)

**Important**: Each Advent of Code participant receives unique input files. The solutions in this repository were written for my specific input files. While the algorithms should work for any valid input, you'll need to use your own input files to get the correct answers for your account.

### Running Tests

Some days include test files. Run them with:

```bash
python test_day13_verify.py
```

## License

See the LICENSE file for details.
