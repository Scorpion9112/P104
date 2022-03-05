import csv

with open("heightWeight.csv") as f:
    dataReader=csv.reader(f)
    allData=list(dataReader)

allData.pop(0)

heightData=[]
for i in range(len(allData)):
    heightValue=allData[i][2]
    heightData.append(float(heightValue))

heightData.sort()
n=len(heightData)

if n%2==0:
    median1=float(heightData[n//2])
    median2=float(heightData[n//2-1])
    median=(median1+median2)/2
else:
    median=heightData[n//2]

print(median)