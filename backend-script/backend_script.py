def print_parking_lot(parking_lot):
    for row in parking_lot:
        print(" | ".join(row))
    print()

def rotate_counterclockwise(direction):
    return {'>': '^', '^': '<', '<': 'v', 'v': '>'}[direction]

def rotate_clockwise(direction):
    return {'>': 'v', 'v': '<', '<': '^', '^': '>'}[direction]

def move_forward(x, y, direction):
    if direction == '>':
        return x, y + 1
    elif direction == '<':
        return x, y - 1
    elif direction == '^':
        return x - 1, y
    elif direction == 'v':
        return x + 1, y

# Initial state
parking_lot = [
    ['_', '_', '_', '_'],
    ['_', '_', '_', '_'],
    ['_', '_', '_', '_'],
    ['_', '_', '>', '_']
]

x, y = 3, 2  # Initial position of the car
direction = '>'  # Initial direction of the car
steps = 0

print("Initial state:")
print_parking_lot(parking_lot)

for _ in range(5):
    # Check the slot behind the car
    if direction == '>':
        behind_x, behind_y = x, y - 1
    elif direction == '<':
        behind_x, behind_y = x, y + 1
    elif direction == '^':
        behind_x, behind_y = x + 1, y
    elif direction == 'v':
        behind_x, behind_y = x - 1, y

    if 0 <= behind_x < 4 and 0 <= behind_y < 5 and parking_lot[behind_x][behind_y] == '_':
        direction = rotate_counterclockwise(direction)
    else:
        direction = rotate_clockwise(direction)

    # Move the car forward
    new_x, new_y = move_forward(x, y, direction)
    if 0 <= new_x < 4 and 0 <= new_y < 5:
        parking_lot[x][y] = 'x' if steps % 2 == 1 else '_'
        x, y = new_x, new_y
        parking_lot[x][y] = direction
        steps += 1

    print(f"iteration {steps}:")
    print_parking_lot(parking_lot)