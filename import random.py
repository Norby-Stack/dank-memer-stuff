import random

for i in range(67):
    add = 0
    for i in range(67):
        add += random.randint(1, 100)
    print(add/67)