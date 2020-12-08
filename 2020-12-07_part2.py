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


def count_total_bags(bags, i):
    for bag in bags:
        if bag != "shiny gold":
            pass
        i += bags[bag]
        print()
        count_total_bags(outer_bags[bag], i)

    return i


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

    # part2
    # get a list of the bags that contain "shiny gold"
    bags_with_gold = []
    for bag in outer_bags:
        # print(bag)
        if contains_shiny_gold(outer_bags[bag]):
            bags_with_gold.append(bag)

    # print(bags_with_gold)

    total_sum = 0
    for bags in outer_bags["shiny gold"]:
        count = count_total_bags(outer_bags[bags], 0)
        print(f"count {bags}: {count}")
        total_sum += outer_bags["shiny gold"][bags] * count_total_bags(
            outer_bags[bags], 0
        )
        total_sum += outer_bags["shiny gold"][bags]
        print()

    print(total_sum)
    # print(outer_bags['shiny gold'])

    # print(count_total_bags(outer_bags[''], 0))
