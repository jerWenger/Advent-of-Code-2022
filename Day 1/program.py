import pandas as pd
import numpy as np

with open('Input.txt') as f:
    file = f.readlines()

max = 0
current = 0

for lines in file :
    
    if lines == "\n":
        if current > max:
            max = current

        current = 0
    else:
        current += int(lines[0:-1])


print(max)



    

