from collections import deque

# the starting numbers

# 436
# numbers = deque([0,3,6])

# 1
# numbers = deque([1,3,2])

# 10
# numbers = deque([2,1,3])

numbers = deque([5, 2, 8, 16, 18, 0, 1])

while True:
    # copy the numbers, get the last number in the list
    last_spoken = numbers.pop()

    # check if the that last number is in the list
    if last_spoken in numbers:
        numbers.append(last_spoken)
        spoken = [index for index, value in enumerate(numbers) if value == last_spoken]
        # get the last two indexes
        val1 = spoken[-1] + 1
        val2 = spoken[-2] + 1

        val3 = val1 - val2
        numbers.append(val3)

    else:
        numbers.append(last_spoken)
        numbers.append(0)

    if len(numbers) == 2020:
        break

print()
print(numbers[-1])
