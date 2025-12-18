from pathlib import Path

### Input ###

input = open(f"{Path(__file__).parent.absolute()}/input.txt", "r").read()

### Solution ###

tiles = [list(map(int, box.split(','))) for box in input.split('\n')]
tiles.append(tiles[0])

rows = []
columns = []
for i in range(len(tiles)-1):
    x1, y1 = tiles[i]
    x2, y2 = tiles[i+1]
    if x1 == x2:
        columns.append((min(y1, y2), max(y1, y2), x1))
    elif y1 == y2:
        rows.append((min(x1, x2), max(x1, x2), y1))

# find intersections of rows and columns
# intersections = set()
# for r in rows:
#     y1, y2, x = r
#     for c in columns:
#         x1, x2, y = c
#         if x1 < x < x2 and y1 < y < y2:
#             intersections.add((y,x))

# print(len(intersections))

def check_if_row_or_column_goes_inside_the_square(x1, y1, x2, y2):
    for r in rows:
        rx1, rx2, ry = r
        if y1 < ry < y2 and not (rx2 <= x1 or rx1 >= x2):
            return True
    for c in columns:
        cy1, cy2, cx = c
        if x1 < cx < x2 and not (cy2 <= y1 or cy1 >= y2):
            return True
    return False

def calculate_amount_of_rows_crossed(x, y):
    y1 = 0
    y2 = y
    counter = 0
    for r in rows:
        rx1, rx2, ry = r
        if y1 <= ry <= y2 and rx1 <= x < rx2:
            counter += 1
    
    return counter

max_square = 0
for i in range(len(tiles) - 1):
    x1, y1 = tiles[i]
    for j in range(i + 1, len(tiles)):
        x2, y2 = tiles[j]
        # print(f"Checking square: ({x1},{y1}) to ({x2},{y2})")
        if check_if_row_or_column_goes_inside_the_square(min(x1, x2), min(y1, y2), max(x1, x2), max(y1, y2)):
            # print("  Square invalid due to row/column inside")
            continue

        # check how many lines to cross if go straight to the side from the top left corner
        if calculate_amount_of_rows_crossed(min(x1, x2), min(y1, y2)) % 2 == 0:
            # print("  Square invalid due to even rows crossed")
            continue

        square = (abs(x1 - x2) + 1) * (abs(y1 - y2) + 1)
        max_square = max(max_square, square)

print(max_square)