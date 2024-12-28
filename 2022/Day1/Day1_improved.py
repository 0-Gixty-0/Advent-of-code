def calc(path):
    with open(path, 'r') as f:
        lines = f.read()
        nums = lines.splitlines()

    totals = []
    cals = 0

    for num in nums:
        if num != "":
            cals += int(num)
        else:
            totals.append(cals)
            cals = 0
    totals.append(cals)
    
    totals.sort()
    print(totals[-1] + totals[-2] + totals[-3])
    return totals[-1]
        
print(calc("Day1/input.txt"))
