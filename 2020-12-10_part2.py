from collections import deque
import functools

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
last_diff = 0

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

        print()

# don't forget the difference between the last adapter and the device ...
# Finally, your device's built-in adapter is always 3 higher than the highest adapter,
# so its rating is 22 jolts (always a difference of 3).
joltage_diffs.append(3)
joltage_diffs_dict[3] += 1

print(joltage_diffs_dict)

# part 2
with open("2020-12-10_input.txt") as input:
    lines = input.read().strip().split("\n")
    lines = list(map(int, lines))
    orig_lines = lines.copy()
    lines.sort()

# start at 0
lines = [0] + lines

adapter_index_updates = []
adapter_index = [1] + [0 for x in range(len(lines) - 1)]
for x in range(len(lines)):
    for y in range(1, 4):
        if lines[x] + y in lines:
            adapter_index[lines.index(lines[x] + y)] += adapter_index[x]
            adapter_index_updates.append(adapter_index[lines.index(lines[x] + y)])

print(adapter_index[-1])

# 3947645370368
