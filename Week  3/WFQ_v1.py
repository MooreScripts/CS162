# Read the file ans assign to a string
q_List = open('input queue.txt', 'r')

# Set up some lists to append to with counters to loop through below
p_q = []
e_q = []
s_q = []
s_count = 0
p_count = 0
e_count = 0

# Loop through lines in the .txt file and assign to a string based off index [0]. Item appended from [1 : end]
for line in q_List:
    filter = line.strip()
    if filter[0] == "P":
        p_q.append(filter[1:])
    elif filter[0] == "E":
        e_q.append(filter[1:])
    elif filter[0] == "S":
        s_q.append(filter[1:])
q_List.close()

# Loop through appended strings to print 3:1 p, 2:1 s, 1:1 e
while s_q or p_q or e_q:
    # Print 3 items from p_q
    while p_count < 3 and p_q:
        print(p_q.pop(0))
        p_count += 1

    # Print 2 items from s_q
    while s_count < 2 and s_q:
        print(s_q.pop(0))
        s_count += 1

    # Print 1 item from e_q
    while e_count < 1 and e_q:
        print(e_q.pop(0))
        e_count += 1

    # Reset the counters and move to the next round
    s_count = 0
    p_count = 0
    e_count = 0
