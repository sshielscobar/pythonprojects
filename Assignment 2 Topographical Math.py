import math
import sys
import time

data = []

with open('C:/Users/sebas/Python/small.txt', 'r') as file:
    for line in file:
        data.append([int(char) for char in line.strip()])

# define step directions
direc = [(-1, 0), (1, 0), (0, 1), (0, -1)]

# define rows and columns
row = len(data)
col = len(data[0])

# find all trail starting points
trail_start = []

for r in range(row):
    for c in range(col):
        if data[r][c] == 0:
            trail_start.append((r, c))

# total popularity counter
total = 0

# go through each starting point
for s in trail_start:
    coords = [s]  # start from this trailhead

    for target in range(1, 10):  # height 1 through 9
        next_coords = []
        for i in range(len(coords)):
            r = coords[i][0]
            c = coords[i][1] 
            for d in range(len(direc)):
                dr = direc[d][0]
                dc = direc[d][1]
                nr = r + dr
                nc = c + dc
                if 0 <= nr < row and 0 <= nc < col:
                    if data[nr][nc] == target:
                        next_coords.append((nr, nc))

        if len(next_coords) == 0:
            coords = []
            break
        coords = next_coords

    # count unique summit cells
    unique = []
    for x in coords:
        if x not in unique:
            unique.append(x)
    total = total + len(unique)

# print total popularity score
print(total)
