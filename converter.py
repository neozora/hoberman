import csv
import json

source = 'data/sample-1.csv'
got_header = True
header = []
body_raw = []

with open(source, 'r') as csvFile:
    reader = csv.reader(csvFile)
  
    for index, row in enumerate(reader):
        
        body_raw.append(row)

        #limit
        if index >= 10:
            break

csvFile.close()

#Header
if got_header == True:
    header = body_raw[0]
    body_raw.pop(0)

print("Header: ")
print(header)
#print("Body: ")
#print(body)
print("Body count: ")
print(len(body_raw))

data = []
cols = []

for i, row in enumerate(body_raw):


print(cols)
        
