"""
--- Day 2: Password Philosophy ---

Your flight departs in a few days from the coastal airport; the easiest way down to the coast from here is via toboggan.

The shopkeeper at the North Pole Toboggan Rental Shop is having a bad day. "Something's wrong with our computers; we can't log in!" You ask if you can take a look.

Their password database seems to be a little corrupted: some of the passwords wouldn't have been allowed by the Official Toboggan Corporate Policy that was in effect when they were chosen.

To try to debug the problem, they have created a list (your puzzle input) of passwords (according to the corrupted database) and the corporate policy when that password was set.

For example, suppose you have the following list:

1-3 a: abcde
1-3 b: cdefg
2-9 c: ccccccccc

Each line gives the password policy and then the password. The password policy indicates the lowest and highest number of times a given letter must appear for the password to be valid. For example, 1-3 a means that the password must contain a at least 1 time and at most 3 times.

In the above example, 2 passwords are valid. The middle password, cdefg, is not; it contains no instances of b, but needs at least 1. The first and third passwords are valid: they contain one a or nine c, both within the limits of their respective policies.

How many passwords are valid according to their policies?
"""

import re

policy = re.compile(r"^(\d{0,})-(\d{0,})\s([a-zA-Z]{1}):\s(\w{0,}$)")

passed = 0

# part 1
with open("2020-12-02_input.txt") as input:
    # with open('2020-12-02_example_input.txt') as input:

    for line in input.readlines():
        line = line.strip("\n")
        # print(line)

        parts = policy.match(line)
        # print(parts.groups())

        search_policy = r"(" + parts.groups()[2] + "{1})"
        search_policy_re = re.compile(search_policy)

        results = search_policy_re.findall(parts.groups()[3])

        # if we get a match object back, then we have results ...
        if results:
            count = len(results)
            if (count >= int(parts.groups()[0])) & (count <= int(parts.groups()[1])):
                # print('PASS!')
                passed += 1

print("passed part 1: {}".format(passed))

# part 2
"""
Exactly one of these positions must contain the given letter. Other occurrences of the letter are irrelevant for the purposes of policy enforcement.

    1-3 a: abcde is valid: position 1 contains a and position 3 does not.
    1-3 b: cdefg is invalid: neither position 1 nor position 3 contains b.
    2-9 c: ccccccccc is invalid: both position 2 and position 9 contain c.

"""

passed = 0

with open("2020-12-02_input.txt") as input:
    # with open('2020-12-02_example_input.txt') as input:
    for line in input.readlines():
        line = line.strip("\n")

        parts = policy.match(line).groups()
        print(parts)

        password = parts[3]

        value = parts[2]

        # i don't know if we'll ever be out of range of the array
        try:
            index_1_val = password[int(parts[0]) - 1]
        except:
            index_1_val = ""

        try:
            index_2_val = password[int(parts[1]) - 1]
        except:
            index_2_val = ""

        val_count = 0
        if index_1_val == value:
            val_count += 1
        if index_2_val == value:
            val_count += 1

        if val_count == 1:
            passed += 1


print("passed part 2: {}".format(passed))


# print(data)
