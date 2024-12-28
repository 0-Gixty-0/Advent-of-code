from aocd import get_data
import re
x = get_data(day=3, year=2024)

sum = 0
do_sum = True
for x in re.finditer(r'do\(\)|don\'t\(\)|mul\((\d{1,3}),(\d{1,3})\)', x):
    match x[0]:
        case 'do()':
            do_sum = True
        case 'don\'t()':
            do_sum = False
        case _:
            if do_sum:
                sum += int(x[1]) * int(x[2])

print(sum)