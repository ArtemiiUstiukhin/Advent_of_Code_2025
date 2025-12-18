from pathlib import Path

### Input ###

input = open(f"{Path(__file__).parent.absolute()}/input.txt", "r").read()

### Solution ###

rows = input.split('\n')
numbers = [list(map(int, row.split())) for row in rows[:-1]]
actions = rows[-1].split()

grand_total = 0
for i in range(len(actions)):
    column_total = 0 if actions[i] == '+' else 1
    for j in range(len(numbers)):
        if actions[i] == '+':
            column_total += numbers[j][i]
        else:
            column_total *= numbers[j][i]
    grand_total += column_total

print(grand_total)