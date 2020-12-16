import re

rules = re.compile(r"^(\w{1,}\s{0,1}\w{0,}):\s(\d{1,})-(\d{1,})\sor\s(\d{1,})-(\d{1,})")
rules_dict = {}

# with open("2020-12-16_test_input2.txt") as input:
with open("2020-12-16_input.txt") as input:
    # read the rules
    line = input.readline().strip("\n")
    while line != "":
        print(line)
        parts = rules.search(line)
        rules_dict[parts.groups()[0]] = []
        rules_dict[parts.groups()[0]].append(
            [i for i in range(int(parts.groups()[1]), int(parts.groups()[2]) + 1)]
        )
        rules_dict[parts.groups()[0]].append(
            [i for i in range(int(parts.groups()[3]), int(parts.groups()[4]) + 1)]
        )

        line = input.readline().strip("\n")

    # read the ticket
    input.readline()
    ticket = list(map(int, [i for i in input.readline().strip("\n").split(",")]))

    # read the nearby tickets
    input.readline()
    input.readline()
    nearby_tickets = []
    line = input.readline().strip("\n")

    while line != "":
        nearby_tickets.append(list(map(int, [i for i in line.split(",")])))
        line = input.readline().strip("\n")

print()

# It doesn't matter which position corresponds to which field; you can
# identify invalid nearby tickets by considering only whether tickets contain
# values that are not valid for any field. In this example, the values on the
# first nearby ticket are all valid for at least one field. This is not true
# of the other three nearby tickets: the values 4, 55, and 12 are are not
# valid for any field. Adding together all of the invalid values produces
# your ticket scanning error rate: 4 + 55 + 12 = 71.

# Consider the validity of the nearby tickets you scanned. What is your
# ticket scanning error rate?

invalid_values = []
invalid_tickets = []

for i, ticket in enumerate(nearby_tickets):
    # print(ticket)
    for value in ticket:
        # print(value)
        valid = False
        # assume the value is INVALID
        # when we find the value in one of the lists, we can return valid
        for rule in rules_dict:
            for rule_range in rules_dict[rule]:
                # print(rule_range)
                if value in rule_range:
                    valid = True
                    break
            if valid:
                break

        if not valid:
            invalid_values.append(value)
            invalid_tickets.append(i)
            print(f"ticket {i}, value {value} valid?: {valid}")

print(invalid_values)
print(sum(invalid_values))

print(f"nearby_tickets: {len(nearby_tickets)}")

# delete the invalid tickets by just reassigning the list based on if the index is in the list:
nearby_tickets = [
    value for i, value in enumerate(nearby_tickets) if i not in invalid_tickets
]

print(f"nearby_tickets: {len(nearby_tickets)}")

# 267, 66, 827, 164, 121, 164, 511, 407, 685, 712, 733, 184, 64, 688
