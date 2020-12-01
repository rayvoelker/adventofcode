with open('2020-12-01_input.txt') as input:
    data = input.readlines()

# with open('2020-12-01_example_input.txt') as input:
#     data = input.readlines()

values = []
for line in data:
    values.append(int(line))

# part 1
for i, value_1 in enumerate(values):
    for j, value_2 in enumerate(values):
        if (i != j):
            # find the sum only if the line numbers aren't the same
            sum = value_1 + value_2
            if (sum == 2020):
                print('found')
                print(value_1 * value_2)
                break

    if (sum == 2020):
        break


# part 2
found = False
for i, value_1 in enumerate(values):
    for j, value_2 in enumerate(values):
        for k, value_3 in enumerate(values):
            if ( (i != j) & (j != k) & (i != k) ):
                sum = value_1 + value_2 + value_3
                if (sum == 2020):
                    found = True
                    print('found')
                    print(value_1 * value_2 * value_3)
        if(found == True):
            break
    if(found == True):
        break
        
        

