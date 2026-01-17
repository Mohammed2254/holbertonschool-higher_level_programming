#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)

lastDegit = abs(number) % 10
if number < 0:
    lastDegit = -lastDegit
if lastDegit > 5:
    print(f"Last digit of {number} is {lastDegit} and is greater than 5")
elif lastDegit == 5:
    print(f"Last digit of {number} is {lastDegit} and is 5")
else:
    print(f"Last digit of {number} is {lastDegit} and is less than 6 and not 0")
