def format_stack_input(path):
    f = open(path,'r')
    strings = []
    for data in f:
        formattedLine = []
        for i in range(getNumberOfStacks(path)):
            formattedLine.append('')
        data = data.rstrip('\n')
        splits = data.split(" ")
        if splits[1].isnumeric():
            break
        else:
            strings.append(reformatSplits(splits))
    f.close()
    return strings

def reformatSplits(splits):
    newSplits = []
    index = 0
    for element in splits:
        if index < len(splits):
            newSplits.append(splits[index])
            try:
                if splits[index+1] == '':
                    index += 4
                else:
                    index += 1
            except Exception:
                break
    return newSplits

def create_stacks(formattedInputArray):
    stacks = []
    for i in range(len(formattedInputArray[0])):
        crates = []
        for list in formattedInputArray:
            if list[i] != '':
                crates.append(list[i])
        stacks.append(crates)
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

def format_instructions(path):
    f = open(path, 'r')
    instructionsArray = []
    for data in f:
        instruction = []
        data = data.rstrip('\n')
        splits = data.split(" ")
        if splits[0] == 'move':
            instruction.append(int(splits[1]))
            instruction.append(int(splits[3]))
            instruction.append(int(splits[5]))
            instructionsArray.append(instruction)
    return instructionsArray

def rearrangeStacks(instructionsArray, stacks):
    for instruction in instructionsArray:
        stacks = move(instruction, stacks)
    return stacks

def move(instruction, stacks):
    load = []
    for i in range(instruction[0]):
        load.append(stacks[instruction[1]-1].pop(0))
    for i in range(1,instruction[0]+1):
        stacks[instruction[2]-1].insert(0,load[-i])
    return stacks

def getAnswer(rearrangedStacks):
    answer = ''
    for stack in rearrangedStacks:
        answer += stack[0]
    return answer

def calculate(path):
    formattedInputArray = format_stack_input(path)
    stacks = create_stacks(formattedInputArray)
    instructionsArray = format_instructions(path)
    rearrangedStacks = rearrangeStacks(instructionsArray, stacks)
    answer = getAnswer(rearrangedStacks)
    return answer

print(calculate('Day5/testinput.txt'))
print(calculate('Day5/input.txt'))