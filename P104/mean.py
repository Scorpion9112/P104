import csv

with open("heightWeight.csv") as f:
    dataReader=csv.reader(f)
    allData=list(dataReader)

allData.pop(0)

heightData=[]
for i in range(len(allData)):
    heightValue=allData[i][2]
    heightData.append(float(heightValue))

total=0
for x in heightData:
    total+=x
    
mean=total/len(heightData)
print(mean)