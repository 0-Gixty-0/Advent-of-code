def format_input_file(path: str) -> list[str]:
    pairs = []
    digits = []
    f = open(path, 'r')
    for data in f:
        data = data.rstrip('\n')
        digits = data.split(",")
        pairs.append(digits)
        digits = []
    f.close()
    return pairs

def calculate2(path):
    pairs = format_input_file(path)
    copies = 0
    for digits in pairs:
        interval1 = digits[0].split('-')
        interval2 = digits[1].split('-')
        if int(interval1[1]) >= int(interval2[0]) and int(interval1[0]) <= int(interval2[1]):
            copies += 1
    return copies

print(calculate2('Day4/testinput.txt'))
print(calculate2('Day4/input.txt'))