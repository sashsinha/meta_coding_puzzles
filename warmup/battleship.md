# Battleship

## Problem Description

You're playing Battleship on a grid of cells with `R` rows and `C` columns. There are `0` or more battleships on the grid, each occupying a single distinct cell. The cell in the `i`-th row from the top and `j`-th column from the left either contains a battleship (`G[i][j] = 1`) or doesn't (`G[i][j] = 0`).

You're going to fire a single shot at a random cell in the grid. You'll choose this cell uniformly at random from the `R * C` possible cells. You're interested in the probability that the cell hit by your shot contains a battleship.

Your task is to implement the function `get_hit_probability(R, C, G)` which returns this probability.

### Constraints
- `1 ≤ R, C ≤ 100`
- `0 ≤ G[i][j] ≤ 1`

### Input
- `R`: Integer, the number of rows in the grid.
- `C`: Integer, the number of columns in the grid.
- `G`: A list of lists of integers (`0` or `1`), representing the grid.

### Output
- A float representing the probability of hitting a battleship. The result must have an absolute or relative error of at most `10^-6` to be considered correct.

### Examples

#### Example 1
**Input:**
```
R = 2
C = 3
G = [
    [0, 0, 1],
    [1, 0, 1]
]
```
**Output:**
```
0.50000000
```

**Explanation:**
There are 3 battleships in the 6-cell grid. The probability of hitting a battleship is `3/6 = 0.5`.

#### Example 2
**Input:**
```
R = 2
C = 2
G = [
    [1, 1],
    [1, 1]
]
```
**Output:**
```
1.00000000
```

**Explanation:**
All 4 cells contain battleships, so the probability of hitting one is `1.0`.

