import math
with open('input.txt') as f:
    inputs = f.readlines()

inputs = [l.strip() for l in inputs]

final = 0
current = 0

for i in inputs:
    fuel = math.floor(int(i)/3)-2
    print('fuel: ' + str(fuel))
    final += fuel
    print('final: ' + str(final))
    current = fuel
    while current > 0:
        if (math.floor(int(current)/3)-2) >= 0:
            current = math.floor(int(current)/3)-2
            final += current
        else:
            current = 0
        print('current: ' + str(current))

print(final)
