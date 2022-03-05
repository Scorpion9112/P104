import csv
from collections import Counter

with open("heightWeight.csv") as f:
    dataReader=csv.reader(f)
    allData=list(dataReader)

allData.pop(0)

heightData=[]
for i in range(len(allData)):
    heightValue=allData[i][2]
    heightData.append(float(heightValue))

countValues=Counter(heightData)

heightRange={
    "75-85":0,
    "85-95":0,
    "95-105":0,
    "105-115":0,
    "115-125":0,
    "125-135":0,
    "135-145":0,
    "145-155":0,
    "155-165":0,
    "165-175":0,
    "175-185":0
}

for height,occurance in countValues.items():
    if 75<float(height)<85:
        heightRange["75-85"]+=occurance
    elif 85<float(height)<95:
        heightRange["85-95"]+=occurance
    elif 95<float(height)<105:
        heightRange["95-105"]+=occurance
    elif 105<float(height)<115:
        heightRange["105-115"]+=occurance
    elif 115<float(height)<125:
        heightRange["115-125"]+=occurance
    elif 125<float(height)<135:
        heightRange["125-135"]+=occurance
    elif 135<float(height)<145:
        heightRange["135-145"]+=occurance
    elif 145<float(height)<155:
        heightRange["145-155"]+=occurance
    elif 155<float(height)<165:
        heightRange["155-165"]+=occurance
    elif 165<float(height)<175:
        heightRange["165-175"]+=occurance
    elif 175<float(height)<185:
        heightRange["175-185"]+=occurance

print(heightRange)