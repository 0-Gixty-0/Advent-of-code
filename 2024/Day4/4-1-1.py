import itertools as it
from aocd import get_data
import re
x = get_data(day=4, year=2024)

rows = x.split('\n')

def check_rows():
    row_count = 0
    for row in rows:
        row_count += row.count("XMAS")
        row_count += row.count("SAMX")
    return row_count

def check_columns():
    column_count = 0
    columns = list(map(list, zip(*rows)))
    for col in columns:
        flattened_col = "".join(col)
        column_count += flattened_col.count("XMAS")
        column_count += flattened_col.count("SAMX")
    return column_count

def check_diagonals():
    diag_count = 0
    rows_len = len(rows)
    cols_len = len(rows[0])
    
    # Top-left to bottom-right diagonals
    for i in range(rows_len - 3):
        for j in range(cols_len - 3):
            diag1 = ''.join([rows[i + k][j + k] for k in range(4)])
            diag_count += diag1.count("XMAS")
            diag_count += diag1.count("SAMX")
    
    # Top-right to bottom-left diagonals
    for i in range(rows_len - 3):
        for j in range(3, cols_len):
            diag2 = ''.join([rows[i + k][j - k] for k in range(4)])
            diag_count += diag2.count("XMAS")
            diag_count += diag2.count("SAMX")
    
    return diag_count

total_count = check_diagonals() + check_rows() + check_columns()
print(total_count)