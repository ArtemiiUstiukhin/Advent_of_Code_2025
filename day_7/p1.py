from pathlib import Path
import queue

### Input ###

input = open(f"{Path(__file__).parent.absolute()}/input.txt", "r").read()

### Solution ###

grid = [list(row) for row in input.split('\n')]

n = len(grid)
m = len(grid[0])

def find_start():
    global grid, n, m
    for i in range(n):
        for j in range(m):
            if (grid[i][j] == 'S'):
                return (i, j)

y, x = find_start()
q = queue.Queue()
q.put((y+1, x))
while not q.empty():
    y, x = q.get()
    if not (0 <= y < n and 0 <= x < m):
        continue
    if grid[y][x] == '|':
        continue
    if grid[y][x] == '.':
        grid[y][x] = '|'
        if y + 1 < n:
            q.put((y+1, x))
    elif grid[y][x] == '^':
        if x - 1 >= 0:
            q.put((y, x-1))
        if x + 1 < m:
            q.put((y, x+1))

split_counter = 0
for i in range(n):
    for j in range(m):
        if (grid[i][j] == '^' and grid[i-1][j] == "|"):
            split_counter += 1

print(split_counter)