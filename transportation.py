def leastCost(opTable, supply, demand):
    sol = 0
    leastCostElement,minRow, minCol = findMin(opTable)
    while True:
        if len(opTable) == 0:
            break
        leastCostElement,minRow, minCol = findMin(opTable)
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
    print("Initial feasible solution is %d"%sol)

def northWest(transTable, supply, demand):
    i, j, sol = 0, 0, 0
    while i != len(transTable) and j != len(transTable[0]):
        if supply[i] == demand[j]:
            sol += demand[j] * transTable[i][j]
            print("%d * %d"%(demand[j],transTable[i][j]))
            demand[i],supply[i], i, j = 0, 0, (i + 1), (j + 1)
        elif supply[i] > demand[j]:
            sol += demand[j] * transTable[i][j]
            print("%d * %d"%(demand[j],transTable[i][j]))
            supply[i] -= demand[j]
            demand[j], j = 0, (j + 1)
        else:
            sol += supply[i] * transTable[i][j]
            print("%d * %d"%(supply[i],transTable[i][j]))
            demand[j] -= supply[i]
            supply[i], i = 0, (i + 1)
    print("Initial feasible solution is %d"%sol)

def insertValues():
    r, c = int(input("Enter Row and Column size of Transportation table: ")), int(input())
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
    return transTable, supply, demand

def checkBalance(supply, demand, transTable):
    if sum(supply) != sum(demand):
        if(sum(supply) > sum(demand)):
            demand.append(sum(supply)-sum(demand))
            for i in range(len(transTable)):
                transTable[i].append(0)
        else:
            supply.append(sum(demand)-sum(supply))
            row = []
            for i in range(len(transTable[0])):
                row.append(0)
            transTable.append(row)
    return supply, demand, transTable

def findMin(tab):
    minValue, minColIndex, minRowIndex = tab[0][0], 0, 0
    for i in range(len(tab)):
        for j in range(len(tab[0])):
            if tab[i][j] < minValue and tab[i][j] != 0:
                minValue, minRowIndex, minColIndex = i, j, tab[i][j]
    return minValue, minRowIndex, minColIndex