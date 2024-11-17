# Write a NumPy program to read a CSV data file and store records in an array.

import numpy as np

f1=open("Data1.csv","w")
f1.write("Hello\n")
f1.write("My\n")
f1.write("name\n")
f1.write("is\n")
f1.write("Ajay")
f1.close()

datalist = []
with open('Data1.csv','r') as f1:
    for i in f1:
        datalist.append(i.strip())
    
data = np.array(datalist)

print(data)
f1.close()

