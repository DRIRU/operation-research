from transportation import*
while True:
    ch = int(input("\n1. North West Corner Method\n2. Least Cost Method\n3. Vogel's Approximation Method\n0. Exit\nEnter Choice: "))
    if ch == 0:
        exit()
    table, supply, demand = insertValues()
    supply, demand, table = checkBalance(supply, demand, table)
    if ch == 1:
        northWest(table, supply, demand)
    elif ch == 2:
        leastCost(table, supply, demand)
    elif ch ==3:
        vogelsApprox(table, supply, demand)
    else:
        print("Wrong Input")
