import csv
CsvFile = csv.reader(open('anketo1e.csv'),delimiter=',')
CsvList = []

for i in CsvFile:
    CsvList.append(i)

print len(CsvList)
for i in range(0,10):
    if len(CsvList[i][5]) != 0:
        print len(CsvList[i][5])

