#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)

lastDeg = abs(number) % 10
if number < 0:
    lastDeg = -lastDeg
if lastDeg > 5:
    print(f"Last digit of {number} is {lastDeg} and is greater than 5")
elif lastDeg == 0:
    print(f"Last digit of {number} is {lastDeg} and is 0")
elif lastDeg < 6 and lastDeg != 0:
    print(f"Last digit of {number} is {lastDeg} and is less than 6 and not 0")
