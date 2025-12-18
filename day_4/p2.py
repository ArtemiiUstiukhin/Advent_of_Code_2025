from pathlib import Path

### Input ###

input = open(f"{Path(__file__).parent.absolute()}/input.txt", "r").read()

### Solution ###

def count_adjacent_rolls(grid, i, j):
    count = 0
    directions = [(-1, -1), (-1, 0), (-1, 1),
                  (0, -1),           (0, 1),
                  (1, -1),  (1, 0),  (1, 1)]
    for di, dj in directions:
        ni, nj = i + di, j + dj
        if 0 <= ni < len(grid) and 0 <= nj < len(grid[0]):
            if grid[ni][nj] == '@':
                count += 1
    return count

grid = [list(row) for row in input.split('\n')]

n = len(grid)
m = len(grid[0])

def remove_rolls(grid):
    rolls_counter = 0
    for i in range(n):
        for j in range(m):
            if (grid[i][j] == '@' and count_adjacent_rolls(grid, i, j) < 4):
                grid[i][j] = '.'
                rolls_counter += 1

    return rolls_counter

total_rolls_removed = 0
while True:
    removed = remove_rolls(grid)
    total_rolls_removed += removed
    if removed == 0:
        break
    
print(total_rolls_removed)