def findMin(tab):
    minValue = tab[0][0]
    minColIndex = minRowIndex = 0
    for i in range(len(tab)):
        for j in range(len(tab[0])):
            if tab[i][j] < minValue and tab[i][j] != 0:
                minValue = tab[i][j]
                minRowIndex = i
                minColIndex = j
    return minValue, minRowIndex, minColIndex

r = int(input("Enter Row and Column size of Transportation table: "))
c = int(input())
print("Enter Elements: ")
transTable = []
for i in range(r):
    row = []
    for j in range(c):
        row.append(int(input()))
    transTable.append(row)

print("Enter the supply values: ")
supply = []
for i in range(r):
    supply.append(int(input()))
print("Enter the demand values: ")
demand = []
for i in range(c):
    demand.append(int(input()))

if sum(supply) != sum(demand):
    if(sum(supply) > sum(demand)):
        demand.append(sum(supply)-sum(demand))
        for i in range(r):
            transTable[i].append(0)
        c += 1
        
    else:
        supply.append(sum(demand)-sum(supply))
        row = []
        for i in range(c):
            row.append(0)
        transTable.append(row)
        r += 1
sol = 0
opTable = transTable
leastCostElement,minRow, minCol = findMin(transTable)
while True:
    if len(opTable) == 0:
        break
    leastCostElement,minRow, minCol = findMin(transTable)
    if supply[minRow] == demand[minCol]:
        sol += demand[minCol] * opTable[minRow][minCol]
        print("%d * %d"%(demand[minCol],opTable[minRow][minCol]))
        demand.pop(minCol)
        supply.pop(minRow)
        opTable.pop(minRow)
        for i in range(len(opTable)):
            opTable[i].pop(minCol)
    elif supply[minRow] > demand[minCol]:
        sol += demand[minCol] * opTable[minRow][minCol]
        print("%d * %d"%(demand[minCol],opTable[minRow][minCol]))
        supply[minRow] -= demand[minCol]
        demand.pop(minCol)
        for i in range(len(opTable)):
            opTable[i].pop(minCol)
    else:
        sol += supply[minRow] * opTable[minRow][minCol]
        print("%d * %d"%(supply[minCol],opTable[minRow][minCol]))
        demand[minCol] -= supply[minRow]
        supply.pop(minRow)
        opTable.pop(minRow)
print (sol)