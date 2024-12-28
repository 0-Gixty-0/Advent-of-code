from aocd import get_data
import re
x = get_data(day=3, year=2024)

sum = 0
matches = re.findall("mul\(\d+,\d+\)",x)

for match in matches:
    value = re.search("\d+.\d+", match).group()
    constants = value.split(',')
    sum += (int(constants[0]) * int(constants[1]))

print(sum)