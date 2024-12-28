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

sum = 0
for update in updates:
    # print('update: ', update)
    validUpdate = True
    for i in range(len(update)):
        if update[i] in list(rules):
            rule_pages = rules[update[i]]
            # print('number to check: ', update[i])
            # print('rule_pages: ', rule_pages)
            if any(page in update[:i] for page in rule_pages):
                validUpdate = False
                break
    if validUpdate:
        sum += update[len(update)//2]
print(sum)