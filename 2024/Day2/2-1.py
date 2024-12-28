from aocd import get_data
x = get_data(day=2, year=2024)

reports = [list(map(int, row.split())) for row in x.splitlines()]

num_safe = 0
for row in reports:
    check_difference = [(row[i], row[i+1]) for i in range(len(row) - 1) 
                    if (abs(row[i] - row[i+1]) < 1) or (abs(row[i] - row[i+1]) > 3)]
    check_all_dec_or_asc = [(-1 if ((row[i] - row[i+1]) > 0) else 1) for i in range(len(row) - 1)]
    if (len(check_difference) <= 0) and (abs(sum(check_all_dec_or_asc)) == (len(row) - 1)):
        num_safe += 1

print(num_safe)
    
