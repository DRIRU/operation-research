def setPenalty(tb):
    rowPen = []
    colPen = []
    for i in range(len(tb)):
        row = sorted(set(tb[i]))
        row = list(row)
        min1, min2 = row[0], row[1]
        rowPen.append(min2-min1)
    for j in range(len(tb[0])):
        col = []
        for i in range(len(tb)):
            col.append(tb[i][j])
        col = sorted(set(col))
        col = list(col)
        min1, min2 = col[0], col[1]
        colPen.append(min2-min1)
    return rowPen, colPen
def findIndex(row, col, tb):
    if max(row) >= max(col):
        i = row.index(max(row))
        j = row.index(min(tb[i]))
    else:
        j = col.index(max(col))
        i = 0
        mini = tab[i][j]
        for n in range(len()): 
            if tb[n][j] < mini:
                mini = tb[n][j]
                i = n
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
opTable = transTable
while True:
    rowPen, colPen = setPenalty(opTable)
