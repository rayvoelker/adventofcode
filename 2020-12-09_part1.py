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


with open("2020-12-09_input.txt") as input:
    lines = input.read().strip().split("\n")
    lines = list(map(int, lines))

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
print(non_match[0])
