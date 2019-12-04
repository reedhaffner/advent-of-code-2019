import math
with open('input.txt') as f:
    inputs = f.readlines()

inputs = [l.strip() for l in inputs]

final = 0

for i in inputs:
    final += math.floor(int(i)/3)-2

print(final)
