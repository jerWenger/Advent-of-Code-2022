import pandas as pd
import numpy as np

with open('Final.txt') as f:
    file = f.readlines()

totals = []

current = 0
for lines in file :
    
    if lines == "\n":
        totals.append(current)
        current = 0
    else:
        current += int(lines[0:-1])

totals.sort()

final = sum(totals[-3:])
print(final)