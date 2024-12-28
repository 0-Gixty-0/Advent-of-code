from aocd import get_data
x = get_data(day=1, year=2024)

splits = x.split()

list1 = []
list2 = []
for i in range(len(splits)):
    if (i % 2 == 0):
        list1.append(int(splits[i]))
    else:
        list2.append(int(splits[i]))

list1.sort()
list2.sort()

sum = 0
for i in range(len(splits) // 2):
    if (list1[i] > list2[i]):
        sum += (list1[i] - list2[i])
    else:
        sum += (list2[i] - list1[i])

print(sum)