lower = 0
upper = 127

columns_lower = 0
columns_upper = 7

boarding_pass = "FBFBBFFRLR"

def seat_id(boarding_pass):
    
    rows = [i for i in range(lower, upper+1)]
    columns = [i for i in range(columns_lower, columns_upper+1)]
    # the first 7 instructions are for moving in the rows...
    for intsruction in boarding_pass[:7]:
        # print(intsruction)
        if intsruction == "F":
            rows = rows[:int(len(rows)/2)]
            # print(rows)
        if intsruction == "B":
            # b - keep the upper half
            rows = rows[int(len(rows)/2):]
            # print(rows)

    # the last three instructions are for moving in the columns ...
    for instruction in boarding_pass[7:]:
        # print(instruction)
        if instruction == "L":
            # keep the upper half
            columns = columns[:int(len(columns)/2)]
            # print(columns)
        if instruction == "R":
            # keep the upper half
            columns = columns[int(len(columns)/2):]
            #print(columns)

    seat_id = rows[0]* 8 + columns[0]
    
    # print(f"{rows[0]}, {columns[0]}")
    # print(f"seat id: {seat_id}")
    
    return seat_id

print(seat_id(boarding_pass))

# find the highest seat id:
seats = []
highest_seat_id = 0
with open("2020-12-05_input.txt") as input:
    for line in input.readlines():
        boarding_pass = line.strip("\n")
        seat_id_val = seat_id(boarding_pass)
        seats.append(seat_id_val)
        # print(f"{boarding_pass} - {seat_id_val}")
        if seat_id_val > highest_seat_id:
            highest_seat_id = seat_id_val
        
print(f"highest_seat_id: {highest_seat_id}")


# part 2
# find the missing seat id in sequence ...
seats.sort()

for i, seat in enumerate(seats):
    try:
        if ( (seats[i] + 1) != seats[i+1]):
            print(f"seats[{i}]: {seats[i]} next: {seats[i+1]}")
            print(f"missing seat: {seats[i] + 1}")
            break
    except:
        pass