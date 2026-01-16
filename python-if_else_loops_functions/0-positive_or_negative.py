#!/usr/bin/python3
import random
number = random.randint(-100, 100)

if number > 0:
    sign = "positive"
elif number == 0:
    sign = "zero"
else:
    sign = "negative"

print(f"{number} is {sign}")
