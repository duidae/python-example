import csv

with open('test.csv', newline='') as csvfile:
    rows = list(csv.reader(csvfile))
    dataRows = rows[1:len(rows)]
    sortRows = sorted(dataRows,key=lambda l:l[0])
    for row in sortRows:
        print(row)
