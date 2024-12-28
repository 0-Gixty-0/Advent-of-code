
# def format_input_file(path: str) -> list[str]:
#     stacks = format_stacks(path)
#     pairs = []
#     digits = []
#     f = open(path, 'r')
#     for data in f:
#         data = data.rstrip('\n')
#         digits = data.split(",")
#         pairs.append(digits)
#         digits = []
#     f.close()
#     return pairs

def format_stack(path):
    stacks = []
    crates = []
    numStacks = getNumberOfStacks(path)
    print(numStacks)
    for stackNum in range(numStacks):
        crates.append(getStack(path,stackNum))
    # for data in f:
    #     if data == '\n':
    #         return stacks
    #     data = data.rstrip('\n')
    #     digits = data.split(",")
    #     pairs.append(digits)
    #     digits = []
    return stacks

def getStack(path,stackNum):
    f = open(path,'r')
    crates = []
    for data in f:
        print('')
        print(crates)
        data = data.rstrip('\n')
        splits = data.split(' ')
        print(splits)
        if splits[stackNum] != '':
            crates.append(splits[stackNum])
        elif splits[-2].isnumeric():
            return crates
    f.close()
    print(crates)
    return crates


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