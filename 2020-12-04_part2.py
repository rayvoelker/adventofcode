import re


expected_fields = {
    'byr': '(Birth Year)',
    'iyr': '(Issue Year)',
    'eyr': '(Expiration Year)',
    'hgt': '(Height)',
    'hcl': '(Hair Color)',
    'ecl': '(Eye Color)',
    'pid': '(Passport ID)',
    'cid': '(Country ID)'
}

for field in expected_fields:
    print(field)


def value_valid(pair):
    key = pair.split(':')[0]
    value = pair.split(":")[1]

    # byr (Birth Year) - four digits; at least 1920 and at most 2002.
    if key == 'byr':
        byr_re = re.compile(r"[0-9]{4}")
        result = byr_re.match(value)
        if result:
            if ( (int(value) >= 1920) & (int(value) <= 2002) ):
                return True

    # iyr (Issue Year) - four digits; at least 2010 and at most 2020.
    if key == 'iyr':
        iyr_re = re.compile(r"[0-9]{4}")
        result = iyr_re.match(value)
        if result:
            if ( (int(value) >= 2010) & (int(value) <= 2020) ):
                return True

    # eyr (Expiration Year) - four digits; at least 2020 and at most 2030
    if key == 'eyr':
        eyr_re = re.compile(r"[0-9]{4}")
        result = eyr_re.match(value)
        if result:
            if ( (int(value) >= 2020) & (int(value) <= 2030) ):
                # print('valid: ', key, value)
                return True

    # hgt (Height) - a number followed by either cm or in:
    # If cm, the number must be at least 150 and at most 193.
    # If in, the number must be at least 59 and at most 76.
    if key == 'hgt':
        hgt_cm_re = re.compile(r"^[0-9]{1,}cm")
        result = hgt_cm_re.match(value)
        if result:
            if ( (int(value[0:-2]) >= 150) & (int(value[0:-2]) <= 193) ):
                return True

        hgt_in_re = re.compile(r"^[0-9]{1,}in")
        result = hgt_in_re.match(value)
        if result:
            if ( (int(value[0:-2]) >= 59) & (int(value[0:-2]) <= 76) ):
                return True

    # hcl (Hair Color) - a # followed by exactly six characters 0-9 or a-f.
    if key == 'hcl':
        hcl_re = re.compile(r"^#[0-9a-f]{6}")
        result = hcl_re.match(value)
        if result:
            return True

    # ecl (Eye Color) - exactly one of: amb blu brn gry grn hzl oth.
    if key == 'ecl':
        ecl_re = re.compile(r"^amb$|^blu$|^brn$|^gry$|^grn$|^hzl$|^oth$")
        result = ecl_re.search(value)
        if result:
            return True

    # pid (Passport ID) - a nine-digit number, including leading zeroes.
    if key == 'pid':
        pid_re = re.compile(r"^[0-9]{9}$")
        result = pid_re.match(value)
        if result:
            return True

    if key == 'cid':
        return True

    return False


def validate(passport):
    # consider cid a met requirement
    try:
        passport.pop('cid')
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
# with open("2020-12-04-example_input_valid.txt") as data:
# with open("2020-12-04-example_input_invalid.txt") as data:
with open("2020-12-04-input.txt") as data:
    # assume the first line we read is new record
    print('\nNEW RECORD', end = ': ')
    passport = expected_fields.copy()
    passports_count = 0
    for line in data:
        if (line.strip("\n") == ''):
            # check the previous passport to see what's missing.
            if validate(passport):
                valid_passports += 1

            print('\nNEW RECORD', end = ': ')

            passport = expected_fields.copy()
            passports_count += 1
        else:
            pairs = line.strip("\n").split(" ")
            for pair in pairs:
                print(pair, end=' ')
                if ( value_valid(pair) ):
                    passport.pop(pair.split(":")[0])

    # check the previous passport to see what's missing.
    if validate(passport):
        valid_passports += 1

print('\n\nvalid_passports:{}'.format(valid_passports))
                
        

