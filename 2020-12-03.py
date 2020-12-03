from collections import deque

hit = 0
hill = []
# with open('day_3_test.txt') as input:
with open("day_3.txt") as input:

    for line in input.readlines():
        hill.append(deque(line.strip("\n")))

rotate_val = -3
print("hill len:", len(hill))

for i in range(1, len(hill)):
    for j in range(len(hill)):
        hill[j].rotate(rotate_val)

    if hill[i][0] == "#":
        hit += 1

print("{} trees hit".format(hit))


# part 2
"""
Determine the number of trees you would encounter if, for each of the 
following slopes, you start at the top-left corner and traverse the map all 
the way to the bottom:

    Right 1, down 1.
    Right 3, down 1. (This is the slope you already checked.)
    Right 5, down 1.
    Right 7, down 1.
    Right 1, down 2.
"""


def trees_hit(move_right, skip_one_down=False):
    hit = 0
    hill = []
    #     with open('day_3_test.txt') as input:
    with open("day_3.txt") as input:

        for line in input.readlines():
            hill.append(deque(line.strip("\n")))

    rotate_val = move_right * -1
    # print('hill len:', len(hill))

    if skip_one_down:
        start = 2
        step = 2
    else:
        start = 1
        step = 1

    for i in range(start, len(hill), step):
        for j in range(len(hill)):
            hill[j].rotate(rotate_val)

        if hill[i][0] == "#":
            hit += 1

    return hit


print(trees_hit(1))
print(trees_hit(3))
print(trees_hit(5))
print(trees_hit(7))
print(trees_hit(1, skip_one_down=True))

print(
    trees_hit(1)
    * trees_hit(3)
    * trees_hit(5)
    * trees_hit(7)
    * trees_hit(1, skip_one_down=True)
)
