
L1 = [[],[4],(1,2),[3,4],(5,6,7)]

resultList = list(L1)  #aby listy miały taką samą długość 

for i in range(len(L1)):
    resultList[i] = 0
    for j in range(len(L1[i])):
        resultList[i] += L1[i][j]

print(resultList)