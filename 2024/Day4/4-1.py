import itertools as it
from aocd import get_data
import re

# DOES NOT WORK

# x = get_data(day=4, year=2024)

# x = """MMMSXXMASM
# MSAMXMSMSA
# AMXSXMAAMM
# MSAMASMSMX
# XMASAMXAMM
# XXAMMXXAMA
# SMSMSASXSS
# SAXAMASAAA
# MAMMMXMMMM
# MXMXAXMASX"""
# x = """SAMS
# XMAS
# XMAS
# XMAS"""

# x = """ S A M S
#         X M A S
#         X M A S
#         X M A S"""

x = """....XXMAS.
.SAMXMS...
...S..A...
..A.A.MS.X
XMASAMX.MM
X.....XA.A
S.S.S.S.SS
.A.A.A.A.A
..M.M.M.MM
.X.X.XMASX"""

rows = x.split('\n')

def checkRow(block):
    count = 0
    row = "".join(block)
    count += row.count("XMAS")
    count += row.count("SAMX")
    return count
    
def checkColumn(block):
    count = 0
    for i in range(4):
        column = "".join([block[j] for j in range(i, len(block), 4)])
        count += column.count("XMAS")
        count += column.count("SAMX")
    return count

def checkDiagonal(block):
    count = 0
    diag1 = "".join([block[i] for i in range(0, len(block), 5)])
    count += diag1.count("XMAS")
    count += diag1.count("SAMX")

    diag2 = "".join(block[i] for i in range(0, len(block), 3))
    count += diag2.count("XMAS")
    count += diag2.count("SAMX")
    return count

def checkBlock(block):
    block_count = 0
    col_count = checkColumn(block)
    row_count = checkRow(block)
    diag_count = checkDiagonal(block)
    block_count = block_count + col_count + row_count + diag_count
    return block_count

def createBlock(indexPairs):
    block = []
    for pair in indexPairs:
        block.append(rows[pair[0]][pair[1]])
    return block

total_count = 0
for i in range(0, len(rows) - 3):
    row_indexes = [i,i+1,i+2,i+3]
    for j in range(0, len(rows[1]) - 3):
        column_indexes = [j,j+1,j+2,j+3]
        cross_indexes = it.product(row_indexes, column_indexes)
        block = createBlock(cross_indexes)
        total_count += checkBlock(block)

print(total_count)