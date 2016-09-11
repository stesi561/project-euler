#! /usr/bin/env python3


tri = []
tri_sum = []
route = []

with open("triangle.txt",'r') as f:
    for line in f:
        line = line.strip()
        tri.append([int(x) for x in line.split(' ')])
        tri_sum.append([0 for x in line.split(' ')])
        route.append([0 for x in line.split(' ')])

tri_sum[len(tri_sum)-1] = tri[len(tri)-1]

#
# Tri:
#
#    a                [0][0]
#   b c         [1][0]      [1][1]
#  d e f  [2][0]      [2][1]      [2][2]
#
# tri_sum[y][x] = tri[y][x] + max(tri_sum[y+1][x], tri_sum[y+1][x+1])
#
# For bottom row of tri_sum - tri_sum[max][x] = tri[max][x]

y = len(tri)-2;
while y >= 0:
    x = 0    
    while x < (len(tri_sum[y+1])-1):
        if(tri_sum[y+1][x] > tri_sum[y+1][x+1]):
            route[y][x] = (y+1,x)
            tri_sum[y][x] = tri[y][x] + tri_sum[y+1][x]
        else:
            route[y][x] = (y+1,x+1)
            tri_sum[y][x] = tri[y][x] + tri_sum[y+1][x+1]            
        x+= 1    
    y-= 1

getting = route[0][0]
pathway = [tri[0][0]]
while getting != 0:
    pathway.append(tri[getting[0]][getting[1]])
    getting = route[getting[0]][getting[1]]

for x in pathway:
    print(x)

print("sum: {}".format(sum(pathway)))

