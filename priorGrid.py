#!/usr/bin/env python
# coding = UTF-8
import numpy as np

newtype = np.dtype({
    'names':['name','value'],
    'formats':[(str,32),'i']
    })

reply = input('How many objects?\n')
objects = np.zeros((int(reply),), dtype = newtype)
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
        reply = input('Is [' + objects[i][0] +
                      '] more important than [' + objects[j][0] + '] ?\n')
        if reply == 'y': objects[i]['value'] += 1
        if reply == 'n': objects[j]['value'] += 1
        i += 1
    j_count += 1
    if j_count == len(objects): break

objects.sort(order = 'value')
print(objects)
