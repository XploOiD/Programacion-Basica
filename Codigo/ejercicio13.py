import random
symbols = ["#","*","@","&"]
for y in range(10):
    line = ""
    for x in range(10):
        line += random.choice(symbols) + ""
        print(line)