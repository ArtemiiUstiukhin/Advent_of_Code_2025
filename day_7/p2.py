from pathlib import Path
import queue
from heapq import heappush, heappop

### Input ###

input = open(f"{Path(__file__).parent.absolute()}/input.txt", "r").read()

### Solution ###

class Node:
    def __init__(self, pos, path_count=0):
        self.pos = pos
        self.next = []
        self.path_count = path_count

    def appendNext(self, edge):
        self.next.append(edge)

    def addPathCount(self, count):
        self.path_count += count

grid = [list(row) for row in input.split('\n')]

n = len(grid)
m = len(grid[0])

def find_start():
    global grid, n, m
    for i in range(n):
        for j in range(m):
            if (grid[i][j] == 'S'):
                return (i, j)

q = queue.Queue()
diGraph = {}

y, x = find_start()
startNode = Node((y, x), 1)

diGraph[(y, x)] = startNode
endNode = Node((n, m))
diGraph[(n, m)] = endNode

q.put((y, x, startNode))

pq = []
heappush(pq, (y, x, startNode))

while not q.empty():
    y, x, lastEdge = q.get()

    # move down until meet a '^' or out of bounds
    while y < n and grid[y][x] != '^':
        y += 1

    if y == n:
        lastEdge.appendNext(endNode)
        continue

    if (y, x) in diGraph:
        lastEdge.appendNext(diGraph[(y, x)])
        continue
    
    node = Node((y, x))
    diGraph[(y, x)] = node
    lastEdge.appendNext(node)
    heappush(pq, (y, x, node))

    if x - 1 >= 0:
        q.put((y, x-1, node))
    if x + 1 < m:
        q.put((y, x+1, node))

print(f"Part 1: {len(pq)-1} (Amount of nodes excluding start and end)")

while len(pq) > 0:
    y, x, node = heappop(pq)
    for nextEdge in node.next:
        nextEdge.addPathCount(node.path_count)

print(f"Part 2: {endNode.path_count} (Amount of distinct paths from start to the end)")