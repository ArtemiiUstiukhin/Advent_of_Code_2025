from pathlib import Path

### Input ###

input = open(f"{Path(__file__).parent.absolute()}/input.txt", "r").read()

### Solution ###

rows = input.split('\n')
actions = rows[-1]

n = len(actions)
m = len(rows) - 1
last_block_index = n - 1
grand_total = 0
for i in range(n):
    pos = n - 1 - i
    if actions[pos] == ' ':
        continue

    block_total = 0 if actions[pos] == '+' else 1
    for j in range(last_block_index, pos - 1, -1):
        number = int(''.join(rows[k][j] for k in range(m)))
        if actions[pos] == '+':
            block_total += number
        else:
            block_total *= number

    last_block_index = pos - 2
    grand_total += block_total
    
print(grand_total)