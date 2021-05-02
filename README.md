# Automataion With Python 

## Format Strings 
```python
my_name = 'ibrahim'
my_age = 20
print(f'My name is {my_name.capitalize()} and my age is {my_age} ')
```
## Args 

using `sys` 

```python
import sys
for arg in reversed(sys.argv[1:]):
  print(arg, end='\t')
```
```bash
>>> python3 file.py 1 2 3 
1     2       3 

We can use argprase for more advanced usage.
```python
import argprase 

parser = argparse.ArgumentParser()
```
To be completed. Can sm1 help?
