#!/usr/bin/python3 

import subprocess
import os
from itertools import product,permutations
from string import digits, ascii_letters

for i in product(ascii_letters,repeat=4):
  print(''.join(i))

