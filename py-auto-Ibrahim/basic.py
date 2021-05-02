#!/usr/bin/env python3 
import time 
import sys 
import os 

for file in os.listdir("img"):
  if os.path.splitext(file)[1] == '.png':
    os.system(f'feh img/{file}')