from pathlib import Path

### Input ###

input = open(f"{Path(__file__).parent.absolute()}/input.txt", "r").read()

### Solution ###

entries = input.split('\n\n')
presents = entries[:-1]
regions = entries[-1].split('\n')

counter = 0
for region in regions:
    region_shape, presents_count = region.split(': ')
    x, y = map(int, region_shape.split('x'))
    presents_count = list(map(int, presents_count.split(' ')))
    # check if all presents fit in the region with no intersections (each present is 3x3)
    if sum(presents_count) // (x // 3) <= (y // 3):
        counter += 1

print(counter)