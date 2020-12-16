from collections import deque

# the starting numbers

# 436
numbers = deque([0, 3, 6])
numbers = dict([(value, i) for i, value in enumerate([0, 3, 6])])


count = len(numbers)
last_spoken = numbers.popitem()
while True:
    print()
    if numbers.get(last_spoken[0]):
        index = numbers.get(last_spoken[0])
        # last spoken now becomes the distance between
        numbers.update({last_spoken[0]: count})
        last_spoken = {(count - index): 0}
    else:
        numbers.update({last_spoken[0]: last_spoken[1]})
        numbers.update({0: count})

    count += 1

    # find the last spoken number
# numbers = dict()

# # numbers = deque([5, 2, 8, 16, 18, 0, 1])

# while True:
#     # copy the numbers, get the last number in the list
#     last_spoken = numbers.pop()

#     # check if the that last number is in the list
#     if last_spoken in numbers:
#         numbers.append(last_spoken)
#         spoken = [index for index, value in enumerate(numbers) if value == last_spoken]
#         # get the last two indexes
#         val1 = spoken[-1] + 1
#         val2 = spoken[-2] + 1

#         val3 = val1 - val2
#         numbers.append(val3)

#     else:
#         numbers.append(last_spoken)
#         numbers.append(0)

#     if len(numbers) == 2020:
#         break

# print()
# print(numbers[-1])
