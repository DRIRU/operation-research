from transportation import*
while True:
    ch = int(input("1. North West Corner Method\n2. Least Cost Method\n3. Exit\nEnter Choice: "))
    table, supply, demand = insertValues()
    supply, demand, table = checkBalance(supply, demand, table)
    if ch == 1:
        northWest(table, supply, demand)
    elif ch == 2:
        leastCost(table, supply, demand)
    elif ch == 3:
        exit()
    else:
        print("Wrong Input")