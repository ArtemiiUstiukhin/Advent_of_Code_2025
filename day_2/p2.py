from pathlib import Path

### Input ###

input = open(f"{Path(__file__).parent.absolute()}/input.txt", "r").read()

### Solution ###

def is_invalid_id(id_str):
    half_len = len(id_str) // 2
    for i in range(1, half_len + 1):
        pattern = id_str[:i]
        if pattern * (len(id_str) // i) == id_str:
            return True
    return False

ranges = input.split(',')
invalid_id_sum = 0
for id_range in ranges:
    start, end = map(int, id_range.split('-'))
    for id in range(start, end + 1):
        if is_invalid_id(str(id)):
            invalid_id_sum += id

print(invalid_id_sum)