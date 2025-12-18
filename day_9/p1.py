from pathlib import Path
from heapq import heappush, heappop

### Input ###

input = open(f"{Path(__file__).parent.absolute()}/input.txt", "r").read()

### Solution ###

tiles = [list(map(int, box.split(','))) for box in input.split('\n')]

max_square = 0
for i in range(len(tiles) - 1):
    for j in range(i + 1, len(tiles)):
        square = (tiles[i][0] - tiles[j][0] + 1) * (tiles[i][1] - tiles[j][1] + 1)
        max_square = max(max_square, square)

print(max_square)