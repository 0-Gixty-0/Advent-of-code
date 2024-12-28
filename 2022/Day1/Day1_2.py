
def format_input_file(path: str) -> list[str]:
    nums = []
    elf_iv = []
    f = open(path, 'r')
    for data in f:
        if data == '\n':
            nums.append(elf_iv)
            elf_iv = []
        else:
            data = data.rstrip('\n')
            elf_iv.append(data)
    nums.append(elf_iv)
    f.close()
    return nums

def calculate_totals(nums) -> list[int]:
    totals = []
    cal_total = 0
    for elf in nums:
        for num in elf:
            num = int(num)
            cal_total += num
        totals.append(cal_total)
        cal_total = 0
    return totals



def calculate_three_highest_total_cal(totals: list[int]):
    totals.sort()
    grandtotal = 0
    for i in range(1,4):
        grandtotal += totals[-i]
    return grandtotal

def main(path) -> int:
    nums = format_input_file(path)
    totals = calculate_totals(nums)
    return calculate_three_highest_total_cal(totals)

print(main("Day1/input.txt"))
# print(main("Day1/testinput.txt"))