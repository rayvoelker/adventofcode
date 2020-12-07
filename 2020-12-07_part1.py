import re

re_bags = re.compile(r"^(\d)\s([a-z]{1,}\s[a-z]{1,})")

outer_bags = {}

# recursive function to find out if the bag has "shiny gold" in any of the children
def contains_shiny_gold(bags):
    for bag in bags:
        if bag == "shiny gold":
            return True
        if contains_shiny_gold(outer_bags[bag]):
            return True
        # print(bag)
    # print()
    return False


# first lets run through the list and fill the outermost bags list. This is also the list of all possible bags
# with open("2020-12-07_test_input.txt") as input:
with open("2020-12-07_input.txt") as input:
    for line in input.readlines():
        line = line.strip("\n")
        bag = line.split(" bags")[0]

        outer_bags[bag] = {}

        contains = line.split(" bags contain ")[1].split(", ")
        if contains[0] != "no other bags.":
            for inner_bag in contains:

                values = re_bags.match(inner_bag)
                # bags_info = {"bag_name": "", "count": 0}
                values = re_bags.match(inner_bag)

                # "bag_name" = values[2]
                # "count_bags = int(values[1])

                outer_bags[bag][values[2]] = int(values[1])

    # find the possible parents for each bag
    found = 0
    for bag in outer_bags:
        # print(bag)
        if contains_shiny_gold(outer_bags[bag]):
            found += 1

    print(f"outer bags contain shiny gold: {found}")
