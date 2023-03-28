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
for i in range(r):
    demand.append(int(input()))
if sum(supply) != sum(supply):
    if(sum(supply) > sum(supply)):
        