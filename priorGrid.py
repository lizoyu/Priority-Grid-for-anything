#!/usr/bin/env python
# coding = UTF-8
import numpy as np

class Error(Exception):
   """Base class for other exceptions"""
pass

class WrongAnswerError(Error):
   """Raised when the input value is wrong"""
pass

newtype = np.dtype({
    'names':['name','value'],
    'formats':[(str,32),'i']
    })

while True:
    try:
        reply = int(input('How many objects? (in numbers)\n'))
    except ValueError:
        print('Please give me the number, like 1, 2, 3.')
        continue
    break

objects = np.zeros((reply,), dtype = newtype)
pointer = 0

while True:
    reply =  input("Please enter the object you want to prioritize:\n")
    objects[pointer][0] = reply
    pointer += 1
    if pointer == len(objects): break

print('Please answer following questions as y or n')

j_count = 1
while True:
    i = 0
    for j in range(j_count, len(objects)):
        while True:
            try:
                reply = input('Is [' + objects[i][0] +
                      '] more important than [' + objects[j][0] + '] ?\n')
                if reply != 'y' and reply != 'n':
                    raise WrongAnswerError
            except WrongAnswerError:
                print('You should answer with y (yes) or n (no).')
                continue
            break
        if reply == 'y': objects[i]['value'] += 1
        elif reply == 'n': objects[j]['value'] += 1
    j_count += 1
    if j_count == len(objects): break

objects.sort(order = 'value')
print(objects)
