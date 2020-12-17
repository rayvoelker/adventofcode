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

print()

# part 2
"""
For example, suppose you have the following notes:

class: 0-1 or 4-19
row: 0-5 or 8-19
seat: 0-13 or 16-19

your ticket:
11,12,13

nearby tickets:
3,9,18
15,1,5
5,14,9

Based on the nearby tickets in the above example, the first position must
be row, the second position must be class, and the third position must be
seat; you can conclude that in your ticket, class is 12, row is 11, and 
seat is 13.

Once you work out which field is which, look for the six fields on your
ticket that start with the word departure. What do you get if you multiply
those six values together?
"""

# start by assume every column in a ticket can be every "rule"

columns = []
for i in range(len(rules_dict)):
    columns.append({"possible_rules": [value for value in rules_dict]})

print()

# find a fit for the first column
# i = 0

for i in range(len(rules_dict)):
    for j, ticket in enumerate(nearby_tickets):
        # print(j, ticket[i])
        for rule_name in rules_dict:
            # print(rule_name)
            if (ticket[i] not in rules_dict[rule_name][0]) and (
                ticket[i] not in rules_dict[rule_name][1]
            ):
                # eliminate rule from column
                # print(f'eliminate {rule_name}')
                columns[i]["possible_rules"] = [
                    value
                    for value in columns[i]["possible_rules"]
                    if value != rule_name
                ]

# find all the columns where possible_rules has a length of 1 and eliminate that value from the other columns
while True:
    target_sum = len(columns)
    targets = [len(value["possible_rules"]) for j, value in enumerate(columns)]

    if sum(targets) == len(columns):
        break

    # columns[i]['possible_rules'] = [value for value in columns[i]['possible_rules'] if value != rule_name]

    # for i, column in enumerate(columns):
    #     if len(column['possible_rules']) == 1:
    #         print(f"{i} {column['possible_rules']} ")
    #         # eliminate that rule from all other columns EXCEPT FOR THIS COLUMN!
    #         print()

    print()
