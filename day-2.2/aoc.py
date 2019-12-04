import math
with open('input.txt') as f:
    the_input = f.read()


intcodes = [int(l.strip()) for l in the_input.split(',')]


def runIntCode(codes):
    intcode = codes
    pointer = 0
    while intcode[pointer] != 99:
        code = intcode[pointer]
        if(code == 1):
            intcode[intcode[pointer+3]] = intcode[intcode[pointer+1]] + \
                intcode[intcode[pointer+2]]
            pointer += 4
        if(code == 2):
            intcode[intcode[pointer+3]] = intcode[intcode[pointer+1]] * \
                intcode[intcode[pointer+2]]
            pointer += 4
    return intcode


noun = 0
verb = 0

while noun <= 99:
    while verb <= 99:
        trycode = intcodes[:]
        trycode[1] = noun
        trycode[2] = verb
        if(runIntCode(trycode)[0] == 19690720):
            print(100*noun + verb)
        verb += 1
    noun += 1
    verb = 0
