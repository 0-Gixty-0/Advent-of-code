import string

def calculate(path):
    total = 0
    chars = []
    chars += list(string.ascii_lowercase)
    chars += list(string.ascii_uppercase)
    backpacks = format_input_file(path)
    for iv in backpacks:
        badItem = getWronglySortedItem(iv)
        value = chars.index(badItem) + 1
        total += value
    return total

def getWronglySortedItem(iv):
    for char in iv[0]:
        if char in iv[1]:
            return char

def format_input_file(path: str) -> list[str]:
    backpacks = []
    iv = []
    f = open(path, 'r')
    for data in f:
        data = data.rstrip('\n')
        n = len(data)
        if n%2 == 0:
            iv.append(data[0:n//2])
            iv.append(data[n//2:])
        else:
            iv.append(data[0:(n//2+1)])
            iv.append(data[(n//2+1):])
        backpacks.append(iv)
        iv = []
    f.close()
    return backpacks

print(calculate("Day3/testinput.txt"))
print(calculate("Day3/input.txt"))