def format_stack(path):
    stacks = []
    crates = []
    numStacks = getNumberOfStacks(path)
    print(numStacks)
    for stackNum in range(numStacks):
        stacks.append(crates)
        crates = []

    f = open(path, 'r')
    for data in f:
        data.rstrip('\n')
        splits = data.split(' ')
        if splits[1].isnumeric():
            return stacks
        else:
            currentStack = 0
            for element in splits:
                if element != '':
                    stacks[currentStack].append(element)
                    currentStack += 1
    print(stacks)
    # for data in f:
    #     if data == '\n':
    #         return stacks
    #     data = data.rstrip('\n')
    #     digits = data.split(",")
    #     pairs.append(digits)
    #     digits = []
    f.close()
    return stacks

def getNumberOfStacks(path):
    numStacks = 0
    f = open(path, 'r')
    for data in f:
        data = data.rstrip('\n')
        splits = data.split(" ")
        if splits[-2].isnumeric():
            f.close()
            return int(splits[-2])
    f.close()
    return 0

def calculate(path):
    stacks = format_stack(path)
    # instructions = format_instructions(path)

print(calculate('Day5/testinput.txt'))