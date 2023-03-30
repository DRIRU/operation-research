def setPenalty(tb):
    rowPen = []
    colPen = []
    for i in range(len(tb)):
        row = sorted(set(tb[i]))
        row = list(row)
        if len(row) == 1 and row[0] == 0:
            min1, min2 = 0 , 0
        else:
            min1, min2 = row[0], row[1]
        rowPen.append(min2-min1)
    for j in range(len(tb[0])):
        col = []
        for i in range(len(tb)):
            col.append(tb[i][j])
        col = sorted(set(col))
        col = list(col)
        if len(col) == 1 and col[0] == 0:
            min1, min2 = 0 , 0
        else:
            min1, min2 = col[0], col[1]
        colPen.append(min2-min1)
    return rowPen, colPen
def findMinColIndex(tb, i):
    mini = 1000
    j = 0
    for n in range(len(tb[0])):
        if tb[i][n] < mini and tb[i][n] != 0:
            mini = tb[i][n]
            j = n
        return j
def findMinRowIndex(tb, j):
    mini = 1000
    i = 0
    for n in range(len(tb)):
        if tb[n][j] < mini and tb[n][j] != 0:
            mini = tb[n][j]
            i = n
        return i
def findIndex(row, col, tb):
    if len(tb) < 2 or len(tb[0]) < 2:
        if len(tb) < 2:
            print(tb)
            i = 0
            j = findMinColIndex(tb, i)
        else:
            j = 0
            i = findMinRowIndex(tb, j)
    elif max(row) >= max(col):
        i = row.index(max(row))
        j = findMinColIndex(tb, i)
    else:
        j = col.index(max(col))
        i = findMinRowIndex(tb, j)
    return i, j

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
        for i in range(len(transTable)):
            transTable[i].append(0)
    else:
        supply.append(sum(demand)-sum(supply))
        row = []
        for i in range(len(transTable[0])):
            row.append(0)
        transTable.append(row)
opTable, sol = transTable, 0
while True:
    if len(opTable) == 0:
        break
    if len(opTable) >= 2 and len(opTable[0]) >= 2: 
        rowPen, colPen = setPenalty(opTable)
    rowIndex, colIndex = findIndex(rowPen, colPen, opTable)
    if supply[rowIndex] == demand[colIndex]:
        sol += demand[colIndex] * opTable[rowIndex][colIndex]
        print("%d * %d"%(demand[colIndex], opTable[rowIndex][colIndex]))
        demand.pop(colIndex)
        supply.pop(rowIndex)
        opTable.pop(rowIndex)
        for i in range(len(opTable)):
            opTable[i].pop(colIndex)
    elif supply[rowIndex] > demand[colIndex]:
        sol += demand[colIndex] * opTable[rowIndex][colIndex]
        print("%d * %d"%(demand[colIndex],opTable[rowIndex][colIndex]))
        supply[rowIndex] -= demand[colIndex]
        demand.pop(colIndex) 
        for i in range(len(opTable)):
            opTable[i].pop(colIndex)
    else:
        sol += supply[rowIndex] * opTable[rowIndex][colIndex]
        print("%d * %d"%(supply[rowIndex],opTable[rowIndex][colIndex]))
        demand[colIndex] -= supply[rowIndex]
        supply.pop(rowIndex)
        opTable.pop(rowIndex)
print("Initial feasible solution is %d"%sol)
