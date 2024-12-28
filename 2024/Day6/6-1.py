from aocd import get_data
x = get_data(day=6, year=2024)

# x = """....#.....
# .........#
# ..........
# ..#.......
# .......#..
# ..........
# .#..^.....
# ........#.
# #.........
# ......#..."""

rows = x.split('\n')
DIRECTIONS = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # (ROW, COL) pairs


def findStartPosition():
    for i in range(len(rows)):
        for j in range(len(rows[0])):
            if rows[i][j] == "^":
                return (i,j)

def turn_right(current_direction):
    current_index = DIRECTIONS.index(current_direction)
    new_index = (current_index + 1) % 4
    return DIRECTIONS[new_index]

def travel(direction, strtPos):
    # print(direction)
    i = strtPos[0] + direction[0]
    j = strtPos[1] + direction[1]
    while rows[i][j] != "#":
        # print("moving to: ", i,j)
        spacesSet.add((i,j))
        i += direction[0]
        j += direction[1]
        if (i > len(rows) - 1 or i < 0) or (j > len(rows[0]) - 1 or j < 0):
            return (False, (i,j))
    return (True, (i - direction[0], j - direction[1]))

position = findStartPosition()
print("start: ", position)
spacesSet = {position}
inBounds = True
direction = DIRECTIONS[3]

while inBounds:
    result = travel(direction, position)
    inBounds = result[0]
    direction = turn_right(direction)
    position = result[1]

print(spacesSet)
print(len(spacesSet))