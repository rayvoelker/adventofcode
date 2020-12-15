from collections import deque

plane = deque([])
with open("2020-12-11_test_input.txt") as input:
    plane = input.read().strip().split("\n")
    print(plane)


def print_plane(plane):
    for line in plane:
        print(line)


def look_right(plane, y, x):
    if (x < 0) or (y < 0):
        return False
    try:
        value = plane[y][x + 1]
    except:
        return False

    return value


def look_left(plane, y, x):
    if (x - 1 < 0) or (y < 0):
        return False
    try:
        value = plane[y][x - 1]
    except:
        return False

    return value


def look_up(plane, y, x):
    if (x < 0) or (y - 1 < 0):
        return False
    try:
        value = plane[y - 1][x]
    except:
        return False

    return value


def look_down(plane, y, x):
    if (x < 0) or (y < 0):
        return False
    try:
        value = plane[y + 1][x]
    except:
        return False

    return value


print_plane(plane)

plane_current_state = plane.copy()
plane_next_state = plane.copy()

value = look_right(plane, 0, 0)

for y in range(len(plane_current_state)):
    # print(y)
    for x in range(len(plane_current_state[y])):
        print(f"y, x = {y}, {x}")

    break
