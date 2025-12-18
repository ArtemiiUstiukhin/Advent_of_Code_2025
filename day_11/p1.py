from pathlib import Path
import queue
from heapq import heappush, heappop

### Input ###

input = open(f"{Path(__file__).parent.absolute()}/input.txt", "r").read()

### Solution ###

class Node:
    def __init__(self, name, path_count=0):
        self.name = name
        self.next = set()
        self.prev = set()
        self.path_count = path_count
        self.distance_from_out = 0

    def appendNext(self, edge):
        self.next.add(edge)

    def appendPrev(self, edge):
        self.prev.add(edge)

    def addPathCount(self, count):
        self.path_count += count

    def updateDistanceFromOut(self, distance):
        self.distance_from_out = min(self.distance_from_out, distance)

entries = input.split('\n')

graph_dict_str = {}
for entry in entries:
    node_name, edges_str = entry.split(': ')
    edges = edges_str.split(' ')
    graph_dict_str[node_name] = edges
graph_dict_str['out'] = []

graph_dict_nodes = {}

q = queue.Queue()
q.put(('you', None))

while not q.empty():
    node_name, parent = q.get()
    
    if node_name in graph_dict_nodes:
        node = graph_dict_nodes[node_name]
    else:
        node = Node(node_name)
        graph_dict_nodes[node_name] = node

    edges = graph_dict_str[node_name]
    for edge in edges:
        q.put((edge, node))

    if parent is not None:
        parent.appendNext(node)
        node.appendPrev(parent)

# Own implementation
q = queue.Queue()
q.put(('out', 0))
while not q.empty():
    node_name, path_count = q.get()
    node = graph_dict_nodes[node_name]
    node.updateDistanceFromOut(path_count)
    for prev_node in node.prev:
        total_path_count = path_count - 1
        q.put((prev_node.name, total_path_count))

q = queue.Queue()
q.put('out')
pq = []
while not q.empty():
    node_name = q.get()
    node = graph_dict_nodes[node_name]
    for prev_node in node.prev:
        item = (prev_node.distance_from_out, prev_node.name)
        if item not in pq:
            heappush(pq, item)
            q.put(prev_node.name)

graph_dict_nodes['you'].path_count = 1

while len(pq) > 0:
    distance, node_name = heappop(pq)
    node = graph_dict_nodes[node_name]
    for nextEdge in node.next:
        nextEdge.addPathCount(node.path_count)

print(f"Part 1: {graph_dict_nodes['out'].path_count} (Amount of distinct paths from YOU to OUT)")