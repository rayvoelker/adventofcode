from collections import OrderedDict

starting_numbers = [0, 3, 6]

# numbers is a dict with the key as the "number" and the value is the position last seen
numbers = OrderedDict([(value, i) for i, value in enumerate(starting_numbers)])

counter = len(numbers)

last_spoken = numbers.popitem(last=True)
while True:

    try:
        print()
        last_seen = numbers[last_spoken[0]]
        last_spoken = (counter + 1) - last_seen[1]
        numbers[last_spoken[0]] = last_spoken

    except:
        print()
        # if there is an no value, re-insert the last spoken and then insert 0
        numbers.update({last_spoken})
        numbers.update({0: counter})

    print()

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
