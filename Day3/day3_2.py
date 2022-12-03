import string

def calculate(path):
    total = 0
    chars = []
    chars += list(string.ascii_lowercase)
    chars += list(string.ascii_uppercase)
    groups = format_input_file(path)
    for backpacks in groups:
        badItem = getBadge(backpacks)
        value = chars.index(badItem) + 1
        total += value
    return total

def getBadge(backpacks):
    for char in backpacks[0]:
        if char in backpacks[1] and char in backpacks[2]:
            return char

def format_input_file(path: str) -> list[str]:
    groups = []
    backpacks = []
    i = 1
    f = open(path, 'r')
    for data in f:
        data = data.rstrip('\n')
        backpacks.append(data)
        if i%3 == 0:
            groups.append(backpacks)
            backpacks = []
        i+=1
    f.close()
    return groups

print(calculate("Day3/testinput.txt"))
print(calculate("Day3/input.txt"))