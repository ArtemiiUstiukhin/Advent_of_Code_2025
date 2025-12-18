from pathlib import Path
import queue

### Input ###

input = open(f"{Path(__file__).parent.absolute()}/input.txt", "r").read()

### Solution ###

class Node:
    def __init__(self, name, path_count=-1):
        self.name = name
        self.next = set()
        self.path_count = path_count
        self.distance_from_out = 0

    def appendNext(self, edge):
        self.next.add(edge)

    def addPathCount(self, count):
        self.path_count = count if self.path_count == -1 else self.path_count + count

    def updateDistanceFromOut(self, distance):
        self.distance_from_out = min(self.distance_from_out, distance)

entries = input.split('\n')

# Parse input into dict structure
graph_dict_str = {}
for entry in entries:
    node_name, edges_str = entry.split(': ')
    edges = edges_str.split(' ')
    graph_dict_str[node_name] = edges
graph_dict_str['out'] = []

# Make linked list
graph_dict_nodes = {}
q = queue.Queue()
q.put(('svr', None))
while not q.empty():
    node_name, parent = q.get()
    if node_name in graph_dict_nodes:
        node = graph_dict_nodes[node_name]
        if parent is not None:
            parent.appendNext(node)
        continue
    
    node = Node(node_name)
    graph_dict_nodes[node_name] = node
    
    if parent is not None:
        parent.appendNext(node)

    edges = graph_dict_str[node_name]
    for edge in edges:
        q.put((edge, node))

# DFS with memoization to count paths
def dfs_count_paths(node, target_node_name, out_node_name=None):
    if out_node_name != None and node.name == out_node_name:
        return 0
    if node.name == target_node_name:
        return 1
    if node.path_count != -1:
        return node.path_count
    
    total_paths = 0
    for next_node in node.next:
        total_paths += dfs_count_paths(next_node, target_node_name, out_node_name)
    
    node.addPathCount(total_paths)
    return total_paths

# Calculate paths for segments: svr -> fft, fft -> dac, dac -> out
start_node_name = 'svr'
target_node_name = 'fft'
total_paths_1 = dfs_count_paths(graph_dict_nodes[start_node_name], target_node_name, 'out')
print(f"Part 2.1: {total_paths_1} (Amount of distinct paths from '{start_node_name}' to {target_node_name})")

# Clean nodes memory
for node_name, node in graph_dict_nodes.items():
    node.path_count = -1

start_node_name = 'fft'
target_node_name = 'dac'
total_paths_2 = dfs_count_paths(graph_dict_nodes[start_node_name], target_node_name, 'out')
print(f"Part 2.2: {total_paths_2} (Amount of distinct paths from '{start_node_name}' to {target_node_name})")

# Clean nodes memory
for node_name, node in graph_dict_nodes.items():
    node.path_count = -1

start_node_name = 'dac'
target_node_name = 'out'
total_paths_3 = dfs_count_paths(graph_dict_nodes[start_node_name], target_node_name)
print(f"Part 2.3: {total_paths_3} (Amount of distinct paths from '{start_node_name}' to {target_node_name})")

print(f"Part 2: {total_paths_1 * total_paths_2 * total_paths_3}")