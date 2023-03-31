import numpy as np
def get_input():
    m = int(input("Enter the number of suppliers: "))
    n = int(input("Enter the number of customers: "))
    supply = np.zeros(m)
    demand = np.zeros(n)
    costs = np.zeros((m, n))
    print("Enter the supply values for each supplier:")
    for i in range(m):
        supply[i] = int(input("Supplier {} supply: ".format(i+1)))
    print("Enter the demand values for each customer:")
    for j in range(n):
        demand[j] = int(input("Customer {} demand: ".format(j+1)))
    for i in range(m):
        for j in range(n):
            costs[i][j] = int(input("Cost for supplier {} and customer {}: ".format(i+1, j+1)))
    print(np.sum(supply))
    print(np.sum(demand))
    if np.sum(supply) != np.sum(demand):
        if np.sum(demand) > np.sum(supply):
            val = np.sum(demand) - np.sum(demand)
            supply = np.append(supply, [val],  axis = 0)
            row = np.zeros((1, m))
            costs = np.append(costs, row, axis = 0)
           
            m += 1
            
        else:
            val =  np.sum(supply) - np.sum(demand)
            demand = np.append(demand, [val],  axis = 0)
            row = np.zeros((n,1))
            costs = np.append(costs, row, axis = 1)
            n += 1
        print(supply)
        print(demand)
        print(costs)
    return supply, demand, costs, m, n
def findMin(tab):
    minValue = 1000
    minColIndex = minRowIndex = 0
    for i in range(len(tab)):
        for j in range(len(tab[0])):
            if tab[i][j] < minValue and tab[i][j] != 0:
                minValue = tab[i][j]
                minRowIndex = i
                minColIndex = j
    return minRowIndex, minColIndex
def northwest_corner(supply, demand, m, n, costs):
    allocation = np.zeros((m, n))
    i = 0
    j = 0
    while i < m and j < n:
        min_val = min(supply[i], demand[j])
        allocation[i][j] = min_val
        supply[i] -= min_val
        demand[j] -= min_val
        if supply[i] == 0:
            i += 1
        if demand[j] == 0:
            j += 1
    total_cost = np.sum(allocation * costs)
    return total_cost

def least_cost1(supply, demand, costs):
    allocation, costArray = [], []
    demand, supply, cost = demand.tolist(), supply.tolist(), costs.tolist()
    while True:
        if len(cost) == 0:
            break
        i, j = findMin(cost)
        allocation.append(min(supply[i], demand[j]))
        costArray.append(cost[i][j])
        supply[i], demand[j] = supply[i] - allocation[len(allocation)-1], demand[j] - allocation[len(allocation)-1]
        if demand[j] == 0:
            demand.pop(j)
            for row in range(len(cost)):
                cost[row].pop(j)
        if supply[i] == 0:
            supply.pop(i)
            cost.pop(i)
    total_cost = 0
    for i in range(len(allocation)):
        total_cost += allocation[i] * costArray[i]
    return total_cost

def main():
    supply, demand, costs, m, n = get_input()
    print("Enter the cost matrix:")
    
    while True:
        print("\nTransportation Problem Solver")
        print("1. Solve using Northwest Corner Method")
        print("2. Solve using Least Cost Method")
        print("3. Quit")
        choice = int(input("Enter choice: "))
        if choice == 1:
            total_cost = northwest_corner(supply, demand, m, n, costs)
            print("Total Cost: ", total_cost)
        elif choice == 2:
            total_cost = least_cost1(supply, demand, costs)
            print("Total Cost: ", total_cost)
        elif choice == 3:
            print("Exiting program...")
            break
        else:
            print("Invalid choice. Please try again.")
main()