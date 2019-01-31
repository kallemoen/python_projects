# Creates a list of lists from txt file
traffic_file = open('traffic.txt', 'r') # Do I need to close this?
traffic_file = traffic_file.readlines()

split_list = []

for line in traffic_file:
    split_list.append(list(line.split(" ")))

# creates a dict with lists of all time entries for each room
time_entries_dict = {}

for item in split_list:
    if item[1] not in time_entries_dict:
        time_entries_dict[item[1]] = []
    if item[2] == 'I':
        negative = -int(item[3])
        time_entries_dict[item[1]].append(negative)
    elif item[2] == 'O':
        positive = int(item[3])
        time_entries_dict[item[1]].append(positive)
    else:
        pass

# calculates average time for each room
avg_time_dict = {}

for key,lis in time_entries_dict.items():
    length = len(lis)
    avg_time_dict[key] = sum(lis)/length

# prints entire dictionary with the right formatting
for key,lis in avg_time_dict.items():
    print("Room {}:".format(int(key)), "{} minutes avg visit,".format(int(lis)), "{} visitor(s) total.".format(int(len(time_entries_dict[key])/2)))
