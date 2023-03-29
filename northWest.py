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
i=0
j=0
sol = 0
while i != r and j != c:
    if supply[i] == demand[j]:
        sol += demand[j] * transTable[i][j]
        print("%d * %d"%(demand[j],transTable[i][j]))
        demand[i],supply[i] = 0,0
        i += 1
        j += 1
    elif supply[i] > demand[j]:
        sol += demand[j] * transTable[i][j]
        print("%d * %d"%(demand[j],transTable[i][j]))
        supply[i] -= demand[j]
        demand[j] = 0
        j += 1
    else:
        sol += supply[i] * transTable[i][j]
        print("%d * %d"%(supply[i],transTable[i][j]))
        demand[j] -= supply[i]
        supply[i] = 0
        i += 1
print("Initial feasible solution is %d"%sol)
