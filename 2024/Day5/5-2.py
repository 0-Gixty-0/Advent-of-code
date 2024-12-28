from aocd import get_data
x = get_data(day=5, year=2024)

# x = """47|53
# 97|13
# 97|61
# 97|47
# 75|29
# 61|13
# 75|53
# 29|13
# 97|29
# 53|29
# 61|53
# 97|53
# 61|29
# 47|13
# 75|47
# 97|75
# 47|61
# 75|61
# 47|29
# 75|13
# 53|13

# 75,47,61,53,29
# 97,61,53,29,13
# 75,29,13
# 75,97,47,61,53
# 61,13,29
# 97,13,75,29,47"""

split_data = x.split('\n')

rules = {}
updates = []

i = 0
while split_data[i] != '':
    pair = split_data[i].split('|')
    if int(pair[0]) in list(rules):
        rules[int(pair[0])].append(int(pair[1]))
    else:
        rules[int(pair[0])] = [int(pair[1])]
    i += 1

for j in range(i+1, len(split_data)):
    updates.append([int(page) for page in split_data[j].split(',')])

# print(rules)
# print(updates)

def fixOrdering(update, rule_pages, j):
    ptr = j
    for i in range(len(update)):
        update[ptr], update[ptr - 1] = update[ptr - 1], update[ptr]
        if any(page in update[:(ptr-1)] for page in rule_pages):
            ptr -= 1
            continue
        else:
            return update


sum = 0
for update in updates:
    newUpdate = []
    invalidUpdate = False
    for i in range(len(update)):
        if update[i] in list(rules):
            rule_pages = rules[update[i]]
            if any(page in update[:i] for page in rule_pages):
                newUpdate.append(update[i])
                newUpdate = fixOrdering(newUpdate, rule_pages, i)
                invalidUpdate = True
            else:
                newUpdate.append(update[i])
        else:
            newUpdate.append(update[i])
                
    if invalidUpdate:
        sum += newUpdate[len(newUpdate)//2]

print(sum)