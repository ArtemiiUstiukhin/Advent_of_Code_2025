from pathlib import Path
import numpy as np
from scipy.optimize import milp, LinearConstraint, Bounds

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

res_sum = 0

for idx, machine in enumerate(machines):
    machine_input = machine.split(' ')
    indicator_lights, buttons, joltage = parce_machine_input(machine_input)

    c = np.array([1 for _ in range(buttons.shape[0])])
    A = np.transpose(buttons)
    b = np.array(joltage)

    # Use milp
    constraints = LinearConstraint(A, b, b)  # A_eq @ x == b
    integrality = np.ones(len(c))  # 1 = integer, 0 = continuous
    bounds = Bounds(0, np.inf)  # x >= 0

    res = milp(c, constraints=constraints, integrality=integrality, bounds=bounds)
    res_sum += int(res.fun)

print(res_sum)