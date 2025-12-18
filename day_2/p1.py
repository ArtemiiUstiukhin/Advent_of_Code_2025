from pathlib import Path

### Input ###

input = open(f"{Path(__file__).parent.absolute()}/input.txt", "r").read()

### Solution ###

def is_invalid_id(id_str):
    if (len(id_str) % 2) != 0:
        return False
    half_len = len(id_str) // 2
    firstpart, secondpart = id_str[:half_len], id_str[half_len:]
    return firstpart == secondpart

ranges = input.split(',')
invalid_id_sum = 0
for id_range in ranges:
    start, end = map(int, id_range.split('-'))
    for id in range(start, end + 1):
        if is_invalid_id(str(id)):
            invalid_id_sum += id

print(invalid_id_sum)