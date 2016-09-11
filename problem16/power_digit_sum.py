#! /usr/bin/env python3


result = pow(2,1000)
result = str(result)
sum = 0
for c in result:
    sum+= int(c)

print(sum)
