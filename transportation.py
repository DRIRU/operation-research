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
    if(sum(supply) < sum(demand)):
        demand.append(sum(demand)-sum(supply))
        row = []
        for i in range(c):
            row.append(0)
        transTable.append(row)
        r += 1
    else:
        supply.append(sum(supply)-sum(demand))
        for i in range(r):
            transTable[i].append(0)
        c += 1
print(transTable)
print(supply)
print(demand)
