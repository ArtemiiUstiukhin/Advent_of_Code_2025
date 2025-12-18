from pathlib import Path

### Input ###

input = open(f"{Path(__file__).parent.absolute()}/input.txt", "r").read()

### Solution ###

def find_max_bank_joltage(bank):
    positions = {}
    
    # Build digits positions map (store first and last occurrence of each digit)
    for i in range(len(bank)):
        joltage = int(bank[i])
        indexes = positions.get(joltage, [])
        if len(indexes) == 0:
            indexes = (i, i)
        else:
            indexes = (indexes[0], i)
        positions[joltage] = indexes
    
    # Iterate from highest to lowest digit to find the best pair
    for i in range(9,0,-1):
        first_num_indexes = positions.get(i, [])
        if len(first_num_indexes) == 0:
            continue
        
        first_num_left, first_num_right = first_num_indexes
        
        # Find the best second number
        for j in range(9,0,-1):
            second_num_indexes = positions.get(j, [])
            if len(second_num_indexes) == 0:
                continue
            second_num_left, second_num_right = second_num_indexes
            if second_num_right > first_num_left:
                return i * 10 + j
            
    return 11
    
banks = input.split('\n')
joltage_sum = 0
for i, bank in enumerate(banks):
    max_joltage = find_max_bank_joltage(bank)
    joltage_sum += max_joltage
    
print(joltage_sum)