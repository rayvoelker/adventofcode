expected_fields = {
    "byr": "(Birth Year)",
    "iyr": "(Issue Year)",
    "eyr": "(Expiration Year)",
    "hgt": "(Height)",
    "hcl": "(Hair Color)",
    "ecl": "(Eye Color)",
    "pid": "(Passport ID)",
    "cid": "(Country ID)",
}

for field in expected_fields:
    print(field)


def validate(passport):
    # consider cid a met requirement
    try:
        passport.pop("cid")
    except:
        pass

    # print(len(passport))
    if len(passport) == 0:
        return True
    else:
        return False
    # print('\t\tmissing: ', end=' ')
    # for field in passport:
    #     print(field, end=', ')


valid_passports = 0

# with open("2020-12-04-example_input.txt") as data:
with open("2020-12-04-input.txt") as data:

    # assume the first line we read is new record
    print("\nNEW RECORD", end=": ")
    passport = expected_fields.copy()
    passports_count = 0
    for line in data:
        if line.strip("\n") == "":
            # check the previous passport to see what's missing.
            if validate(passport):
                valid_passports += 1

            print("\nNEW RECORD", end=": ")

            passport = expected_fields.copy()
            passports_count += 1
        else:
            pairs = line.strip("\n").split(" ")
            for pair in pairs:
                print(pair, end=" ")
                passport.pop(pair.split(":")[0])

    # check the previous passport to see what's missing.
    if validate(passport):
        valid_passports += 1

print("\n\nvalid_passports:{}".format(valid_passports))
