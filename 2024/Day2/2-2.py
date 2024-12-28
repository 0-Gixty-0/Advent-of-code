from aocd import get_data
x = get_data(day=2, year=2024)

reports = [list(map(int, row.split())) for row in x.splitlines()]

def is_safe(row):
    inc = {row[i + 1] - row[i] for i in range(len(row) - 1)}
    return inc <= {1, 2, 3} or inc <= {-1, -2, -3}

safe_count = sum([any([is_safe(row[:i] + row[i + 1:]) for i in range(len(row))]) for row in reports])
print(safe_count)