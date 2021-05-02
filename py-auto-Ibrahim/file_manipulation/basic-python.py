#!/usr/bin/env python3
import time
import sys
import os

'''Loops'''
for i in range(1000):
    time.sleep(0.001)
    print(f'i = {i}')

''' arguments '''
for arg in reversed(sys.argv[1:]):
    print(arg, end=' ')

''' os module'''
files_in_current_dir = sorted(os.listdir("img"))
for file in files_in_current_dir:
    if os.path.splitext(file)[1] == '.png':
        os.system(f'feh {file}')  
