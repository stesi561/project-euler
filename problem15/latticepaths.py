#! /usr/bin/env python3

import sys

sides = int(sys.argv[1])
depth = sides*2+1

rows = []
rows.append([1])
x = 1;
while x < depth:
    next_row = [1]
    y = 1;
    while y < len(rows[-1]):
        next_row.append(rows[-1][y]+rows[-1][y-1])
        y+= 1
    next_row.append(1)
    rows.append(next_row)
    x+= 1
result = max(rows[-1])
#for row in rows:
#    print(" ".join([str(x) for x in row]))
print("For a {sides} by {sides} grid there are {result} paths".format(sides=sides, result=result))
