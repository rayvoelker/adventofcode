from collections import deque

with open("2020-12-10_input.txt") as input:
    lines = input.read().strip().split("\n")
    lines = list(map(int, lines))
    orig_lines = lines.copy()
    lines.sort()
    lines = deque(lines)

print(lines)

joltage_diffs = []
joltage_diffs_dict = {1: 0, 2: 0, 3: 0}
current_joltage = 0

while True:
    try:
        adapter = lines.popleft()
    except:
        break

    current_joltage_range = range(current_joltage + 1, 4)

    print()

    # sanity check
    if adapter in range(current_joltage + 1, current_joltage + 4):
        # print("YES!")
        joltage_diffs.append(adapter - current_joltage)
        joltage_diffs_dict[adapter - current_joltage] += 1
        current_joltage = adapter
# don't forget the difference between the last adapter and the device ...
# Finally, your device's built-in adapter is always 3 higher than the highest adapter,
# so its rating is 22 jolts (always a difference of 3).
joltage_diffs.append(3)
joltage_diffs_dict[3] += 1

print(joltage_diffs_dict)

print(joltage_diffs_dict[1] * joltage_diffs_dict[3])
