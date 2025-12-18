from pathlib import Path
import numpy as np

### Input ###

input = open(f"{Path(__file__).parent.absolute()}/input.txt", "r").read()

### Solution ###

machines = input.split('\n')

def parce_machine_input(machine_input):
    indicator_lights_raw = machine_input[0]
    indicator_lights = np.array([(0 if x == '.' else 1) for x in list(indicator_lights_raw[1:-1])])
    
    buttons_raw = machine_input[1:-1]
    buttons_data = []
    for row in buttons_raw:
        indexes = [int(x) for x in row[1:-1].split(',')]
        matrix_row = [1 if i in indexes else 0 for i in range(indicator_lights.size)]
        buttons_data.append(matrix_row)
    buttons = np.matrix(buttons_data)

    joltage_raw = machine_input[-1]
    joltage = np.array([int(x) for x in joltage_raw[1:-1].split(',')])

    return indicator_lights, buttons, joltage

res = 0

for idx, machine in enumerate(machines):
    machine_input = machine.split(' ')
    indicator_lights, buttons, joltage = parce_machine_input(machine_input)

    min_sol = -1

    # iterate over all solution conbinations arrays consists of 0 and 1
    num_buttons = buttons.shape[0]
    for i in range(2**num_buttons):
        combination = [(i >> bit) & 1 for bit in range(num_buttons)]
        solution = np.transpose(np.array(combination))
    
        target_matrix = np.mod(np.transpose(buttons) @ solution, 2)
        target_row = np.array(target_matrix)[0]
        if np.array_equal(target_row, indicator_lights):
            num_presses = sum(combination)
            if min_sol == -1 or num_presses < min_sol:
                min_sol = num_presses

    res += min_sol

print(res)