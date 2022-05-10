import csv
import numpy as np

with open('avocado.csv') as file:
    content = file.readlines()
matrix=np.asmatrix(content)
header = content[:1]
rows = content[1:]
print(header)
#print(rows)
arra=np.array(header)
for i in range(len(rows)):
    row=rows[i]
    nrow=row.split(", ")
    print(nrow)


