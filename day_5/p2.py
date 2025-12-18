from pathlib import Path

### Input ###

input = open(f"{Path(__file__).parent.absolute()}/input.txt", "r").read()

### Solution ###

ranges, ingredients = input.split('\n\n')
ranges = ranges.split('\n')
ingredients = ingredients.split('\n')

def try_merge_ranges(merged_ranges, new_range):
    l,r = map(int, new_range.split('-'))
    for m in merged_ranges:
        if not (r < m[0] or l > m[1]):
            m[0] = min(m[0], l)
            m[1] = max(m[1], r)
            return True
    return False

# Merge ranges
ranges.sort(key=lambda r: int(r.split('-')[0]))
merged_ranges = []
for range in ranges:
    if not try_merge_ranges(merged_ranges, range):
        l,r = map(int, range.split('-'))
        merged_ranges.append([l,r])

merged_ranges.sort(key=lambda r: r[0])

total_ranges_length = 0
for l,r in merged_ranges:
    total_ranges_length += (r - l + 1)

print(total_ranges_length)