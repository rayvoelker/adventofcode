from collections import deque


def sum_in_preable(preamble, target):
    while True:
        try:
            value = preamble.popleft()
        except:
            break

        # sum the popped value to the remaining values in the preamble...
        # compare it to the target
        # print(preamble, value)
        for i in range(len(preamble)):
            if preamble[i] + value == target:
                return True

    return False


# with open("2020-12-09_test_input.txt") as input:
with open("2020-12-09_input.txt") as input:
    lines = input.read().strip().split("\n")
    lines = list(map(int, lines))

# TODO
# CHANGE THESE BACK AFTER TESTING!!!
preamble = deque(lines[:25])
lines = deque(lines[25:])

print()

non_match = []

while True:
    try:
        target = lines.popleft()
    except:
        break

    # print(f"{target} has sum of two values in ({preamble})?")
    if sum_in_preable(preamble.copy(), target):
        pass
        # print("TRUE!")
    else:
        # print("FALSE")
        # print(target, end=', ')
        non_match.append(target)

    # print()

    # throw away the left most value of the preamble and append the target
    preamble.popleft()
    preamble.append(target)
    # value = lines.pop()

# print(non_match[0])
# i think there should only be one "invalid" number? ...
print(non_match[0])

# part 2
# The final step in breaking the XMAS encryption relies on the invalid number
# you just found: you must find a contiguous set of at least two numbers in
# your list which sum to the invalid number from step 1.

# re-read our input
with open("2020-12-09_input.txt") as input:
    lines = input.read().strip().split("\n")
    lines = deque(map(int, lines))

# find contiguous sum ..
found_sums = []
while True:
    search_list = lines.copy()
    sums_list = []
    while True:
        try:
            sums_list.append(search_list.popleft())
        except:
            break
        if sum(sums_list) > non_match[0]:
            break
        if sum(sums_list) == non_match[0]:
            # if the len sums_list > len found_sums ... swap and break
            if len(sums_list) > len(found_sums):
                found_sums = sums_list
            break
        # print()

    try:
        lines.popleft()
    except:
        break

print(found_sums)

found_sums.sort()

print(found_sums)
print(f"found_sums[0] + found_sums[-1] = {found_sums[0] + found_sums[-1]}")
