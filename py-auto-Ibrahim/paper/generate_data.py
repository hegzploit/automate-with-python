#!/usr/bin/python3

def f(x): return x*x


nums = range(15)
squared = [num * num for num in nums]

with open('data.dat', 'w') as out:
    for x in range(15):
        out.write(f'{x} {f(x)}\n')

with open('data2.dat', 'w') as out:
    for num, suq in zip(nums, squared):
        out.write(f'{num} {suq}\n')
