with open("2020-12-06_input.txt") as input:
    # with open("2020-12-06_test_input.txt") as input:
    answers_dict = {}
    total_sum = 0
    all_yes_total_sum = 0
    member_count = 0
    for line in input.readlines():
        line = line.strip("\n")
        if line == "":
            # if the number of group members appears as the value in the dict,
            # then they all answered "YES"
            for key, value in answers_dict.items():
                if value == member_count:
                    all_yes_total_sum += 1

            print(answers_dict)
            total_sum += len(answers_dict)
            answers_dict = {}
            member_count = 0
            print("---")
        else:
            member_count += 1
            for answer in line:
                print(answer, end=",")
                try:
                    answers_dict[answer] += 1
                except:
                    answers_dict[answer] = 1
    for key, value in answers_dict.items():
        if value == member_count:
            all_yes_total_sum += 1
    total_sum += len(answers_dict)

print(f"\n\ntotal_sum: {total_sum}")
print(f"all_yes_total_sum: {all_yes_total_sum}")
