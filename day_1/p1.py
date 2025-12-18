from pathlib import Path

### Input ###

input = open(f"{Path(__file__).parent.absolute()}/input.txt", "r").read()

### Solution ###

rotations = input.split('\n')
position = 50
zero_counter = 0

for rotation in rotations:
    rotation_side = rotation[0]
    rotation_number = int(rotation[1:]) * (1 if rotation_side == 'R' else -1)
    position = (position + rotation_number) % 100
    if position == 0:
        zero_counter += 1
 
print(zero_counter)