import csv
CsvFile = csv.reader(open('anketo1.csv'),delimiter=',')
CsvList = []

for i in CsvFile:
    CsvList.append(i)

print len(CsvList)
