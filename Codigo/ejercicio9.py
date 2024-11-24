import random

for y in range(10):
    line = "."
    for x in range(10):
        if random.choice([True,False]):
            line += "."
        else:
            line += ""
print(line)               