import functools
 
input_rules = open("a.txt").read()
input_updates = open("b.txt").read()
 
input_rules = [row.split("|") for row in [row for row in input_rules.split("\n")]]
input_updates = [row.split(",") for row in [row for row in input_updates.split("\n")]]
input_updates_num = []
for i, row in enumerate(input_updates):
    input_updates_num.append([])
    for item in row:

        input_updates_num[i].append(int(item))
 
rules_dict = {}
for item in input_rules:
    if int(item[0]) in rules_dict:
        rules_dict[int(item[0])].append(int(item[1]))
    else:
        rules_dict[int(item[0])] = []
 
def compare(x, y):
    if y in rules_dict[x]:
        return -1
    else:
        return 1
    
total_sorted_mid = 0
total_invalid = 0
total_valid = 0
for update in input_updates_num:
    sorted_update = sorted(update.copy(), key=functools.cmp_to_key(compare))
    midpoint = int(len(sorted_update) / 2)
    if update != sorted_update:
        total_sorted_mid += sorted_update[midpoint]
        total_invalid += 1
    else:
        total_valid += update[midpoint]
 
print(total_valid)
print(total_sorted_mid)
print(total_valid + total_sorted_mid)
