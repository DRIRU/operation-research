import java.util.Scanner;

public class transportation {
    
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        
        // Input the number of sources and destinations
        System.out.print("Enter the number of sources: ");
        int m = input.nextInt();
        System.out.print("Enter the number of destinations: ");
        int n = input.nextInt();
        
        // Input the supply and demand arrays
        int[] supply = new int[m];
        int[] demand = new int[n];
        System.out.println("Enter the supply values:");
        for (int i = 0; i < m; i++) {
            supply[i] = input.nextInt();
        }
        System.out.println("Enter the demand values:");
        for (int i = 0; i < n; i++) {
            demand[i] = input.nextInt();
        }
        
        // Input the cost matrix
        int[][] cost = new int[m][n];
        System.out.println("Enter the cost matrix:");
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                cost[i][j] = input.nextInt();
            }
        }
        System.out.println("1.North West Corner\n2.Least Cost Method\nEnter choice: ");
        int ch = input.nextInt();
        if(ch == 1)
        { 
            // Solve using North West Corner Method
            System.out.println("Solution using North West Corner Method:");
            int[][] northWestCorner = solveNorthWestCorner(supply, demand, cost);
            int total = calcTotal(northWestCorner, cost);
            System.out.println("Initial feasible Solution is "+total);
        }
        // Solve using Least Cost Method
        else
        {
            System.out.println("Solution using Least Cost Method:");
            int[][] leastCost = solveLeastCost(supply, demand, cost);
            int total = calcTotal(leastCost, cost);
            System.out.println("Initial feasible Solution is "+total);
        }
    }
    public static int calcTotal(int[][] allocation, int[][] cost)
    {
        int total = 0;
        for(int i = 0; i < cost.length; i++)
        {
            for(int j = 0; j < cost[0].length; j++)
            {   
                total += cost[i][j] * allocation[i][j];
            }
        } 
        return total;
    }
    // Function to solve using North West Corner Method
    public static int[][] solveNorthWestCorner(int[] supply, int[] demand, int[][] cost) {
        int[][] allocation = new int[supply.length][demand.length];
        int i = 0, j = 0;
        while (i < supply.length && j < demand.length) {
            if (supply[i] < demand[j]) {
                allocation[i][j] = supply[i];
                demand[j] -= supply[i];
                i++;
            } else {
                allocation[i][j] = demand[j];
                supply[i] -= demand[j];
                j++;
            }
        }
        return allocation;
    }
    
    // Function to solve using Least Cost Method
    public static int[][] solveLeastCost(int[] supply, int[] demand, int[][] cost) {
        int[][] allocation = new int[supply.length][demand.length];
        while (true) {
            int minCost = Integer.MAX_VALUE;
            int row = -1, col = -1;
            for (int i = 0; i < supply.length; i++) {
                for (int j = 0; j < demand.length; j++) {
                    if (supply[i] > 0 && demand[j] > 0 && cost[i][j] < minCost) {
                        minCost = cost[i][j];
                        row = i;
                        col = j;
                    }
                }
            }
            if (row == -1 || col == -1) {
                break;
            }
            int amount = Math.min(supply[row], demand[col]);
            allocation[row][col] = amount;
            supply[row] -= amount;
            demand[col] -= amount;
        }
        return allocation;
    }

public static void printMatrix(int[][] matrix) {
    for (int i = 0; i < matrix.length; i++) {
        for (int j = 0; j < matrix[0].length; j++) {
            System.out.print(matrix[i][j] + "\t");
        }
        System.out.println();
    }
}
}