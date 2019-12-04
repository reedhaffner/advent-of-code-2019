import math
with open('input.txt') as f:
    the_input = f.read()

intcodes = [int(l.strip()) for l in the_input.split(',')]

pointer = 0

while intcodes[pointer] != 99:
    code = intcodes[pointer]
    print("Pointer: " + str(pointer))
    if(code == 1):
        print('Addition')
        intcodes[intcodes[pointer+3]] = intcodes[intcodes[pointer+1]] + \
            intcodes[intcodes[pointer+2]]
        pointer += 4
    if(code == 2):
        print('Multiplication')
        intcodes[intcodes[pointer+3]] = intcodes[intcodes[pointer+1]] * \
            intcodes[intcodes[pointer+2]]
        pointer += 4
    print(intcodes)
