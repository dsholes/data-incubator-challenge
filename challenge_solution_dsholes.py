import fileinput
import numpy as np

MAL_LINE_STR = "Malformed line, ignoring '{0}'"
OUTPUT_STR = "{0:.3f}, {1:.3f}, {2:.3f}"

x_list=[]

# read line by line from stdin
for line in fileinput.input():
    
    # If line is empty end of file is reached
    if not line:
        break
    
    # Convert line to float, handle malformed lines
    try:
        x = float(line)
    except ValueError:
        print(MAL_LINE_STR.format(line.strip()))
        continue

    # Perform calculations and print results to stdout
    x_list.append(x)
    print(
        OUTPUT_STR.format(
            np.mean(x_list), np.std(x_list), np.median(x_list)
        )
    )
