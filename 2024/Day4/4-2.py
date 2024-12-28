import itertools as it
from aocd import get_data
import re
x = get_data(day=4, year=2024)

rows = x.split('\n')

count = 0
for i in range(1, len(rows) - 1):
    for j in range(1, len(rows[0]) - 1):
        if rows[i][j] == "A":
            diag1 = ""
            diag1 += rows[i - 1][j - 1]
            diag1 += rows[i][j]
            diag1 += rows[i + 1][j + 1]

            diag2 = ""
            diag2 += rows[i - 1][j + 1]
            diag2 += rows[i][j]
            diag2 += rows[i + 1][j - 1]

            if (diag1 == "SAM" or diag1 == "MAS") and (diag2 == "SAM" or diag2 == "MAS"):
                count += 1

print(count)
