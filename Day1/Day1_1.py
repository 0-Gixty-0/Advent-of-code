
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
        
def calculate_highest_total_cal(nums) -> int:
    total = 0
    temp = 0
    for elf in nums:
        for num in elf:
            temp += int(num)
        if temp > total:
            total = temp
        temp = 0
    return total

def main(path) -> int:
    nums = format_input_file(path)
    return calculate_highest_total_cal(nums)

print(main("Day1/input.txt"))
# print(main("Day1/testinput.txt"))