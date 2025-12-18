from pathlib import Path

### Input ###

input = open(f"{Path(__file__).parent.absolute()}/input.txt", "r").read()

### Solution ###

def find_max_bank_joltage(bank, batteries_count):
    # Set init indexes to the last digits
    indexes = [len(bank) - batteries_count + i for i in range(batteries_count)]
    prev_digit_index = -1

    # Move from right to left to maximize each digit starting from the leftmost
    for i, bank_index in enumerate(indexes):
        max_joltage = bank[bank_index]
        for k in range(bank_index, prev_digit_index, -1):
            if int(bank[k]) >= int(max_joltage):
                max_joltage = bank[k]
                indexes[i] = k
        prev_digit_index = indexes[i]
    
    res = "".join([bank[i] for i in indexes])
    return int(res)
    

banks = input.split('\n')
joltage_sum = 0
for i, bank in enumerate(banks):
    max_joltage = find_max_bank_joltage(bank, 12)
    joltage_sum += max_joltage

print(joltage_sum)