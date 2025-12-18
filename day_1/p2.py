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
    target_position = (position + rotation_number)
    zero_pass_count = abs(target_position // 100) if target_position <= 0 else ((target_position -  1) // 100)
    if position == 0 and target_position < 0:
        zero_pass_count -= 1
    position = target_position % 100
    zero_counter += zero_pass_count
    if position == 0:
        zero_counter += 1

print(zero_counter)