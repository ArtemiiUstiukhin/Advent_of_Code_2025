from pathlib import Path
from heapq import heappush, heappop

### Input ###

input = open(f"{Path(__file__).parent.absolute()}/input.txt", "r").read()

### Solution ###

boxes = [list(map(int, box.split(','))) for box in input.split('\n')]
distances = []
for i in range(len(boxes) - 1):
    for j in range(i + 1, len(boxes)):
        pair = tuple(sorted((i, j)))
        distance_squared = sum((boxes[i][k] - boxes[j][k]) ** 2 for k in range(3))
        heappush(distances, (distance_squared, pair))

circuits = []

def find_circuit_containing_box(box_index):
    global circuits
    for circuit in circuits:
        if box_index in circuit:
            return circuit
    return None

while(True):
    distance_squared, (box1, box2) = heappop(distances)
    circuit_that_contains_box1 = find_circuit_containing_box(box1)
    circuit_that_contains_box2 = find_circuit_containing_box(box2)

    if circuit_that_contains_box1 is None and circuit_that_contains_box2 is None:
        circuits.append(set([box1, box2]))
    elif circuit_that_contains_box1 is not None and circuit_that_contains_box2 is None:
        circuit_that_contains_box1.add(box2)
    elif circuit_that_contains_box1 is None and circuit_that_contains_box2 is not None:
        circuit_that_contains_box2.add(box1)
    elif circuit_that_contains_box1 != circuit_that_contains_box2:
        circuit_that_contains_box1.update(circuit_that_contains_box2)
        circuits.remove(circuit_that_contains_box2)
    
    if len(circuits) == 1 and len(circuits[0]) == len(boxes):
        print(boxes[box1][0] * boxes[box2][0])
        break