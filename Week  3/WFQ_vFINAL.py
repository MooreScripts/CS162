from collections import deque

# Read the attached queue.txt file assign to string q_list
q_List = open('input queue.txt', 'r')

# Creating deque objects to append to
p_queue = deque()
e_queue = deque()
s_queue = deque()

# Counters to be used in while loop below
s_count = 0
p_count = 0
e_count = 0

# Looping through q_list checking index 0 of each line, appends to appropriate queue and drops 0 index
for line in q_List:
    queue_assignment = line.strip()
    if queue_assignment[0] == "P":
        p_queue.append(queue_assignment[1:])
    elif queue_assignment[0] == "E":
        e_queue.append(queue_assignment[1:])
    elif queue_assignment[0] == "S":
        s_queue.append(queue_assignment[1:])

print("The premium 3:1 packets queued are:", ', '.join(list(p_queue)))
print("The standard 2:1 packets queued are:", ', '.join(list(s_queue)))
print("The economy 1:1 packets queued are:", ', '.join(list(e_queue)))
# Close the opened .txt file to prevent memory leak
q_List.close()

print("\033[91m" + "initializing queue with above ratios" + "\033[0m")
# Looping the queue's to pop the desired amount of items by incrementing by 1, then resetting counters
while s_queue or p_queue or e_queue:
    if p_count < 3 and p_queue:
        print(p_queue.popleft())
        p_count += 1
    elif s_count < 2 and s_queue:
        print(s_queue.popleft())
        s_count += 1
    elif e_count < 1 and e_queue:
        print(e_queue.popleft())
        e_count += 1
    else:
        # Reset counters for the loop to restart
        s_count = 0
        p_count = 0
        e_count = 0
