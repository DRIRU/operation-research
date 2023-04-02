using System;

public class TransportationProblemSolver
{
    private int[,] transportationMatrix;
    private int[] supply;
    private int[] demand;
    private int[,] allocations;

    public TransportationProblemSolver(int[,] transportationMatrix, int[] supply, int[] demand)
    {
        this.transportationMatrix = transportationMatrix;
        this.supply = supply;
        this.demand = demand;
        this.allocations = new int[supply.Length, demand.Length];
    }

    public void Solve()
    {
        while (HasUnallocatedSupplyOrDemand())
        {
            int[] indices = FindLeastCostCell();
            int supplyIndex = indices[0];
            int demandIndex = indices[1];

            int allocation = Math.Min(supply[supplyIndex], demand[demandIndex]);
            allocations[supplyIndex, demandIndex] = allocation;

            supply[supplyIndex] -= allocation;
            demand[demandIndex] -= allocation;
        }
    }

    public int[,] GetAllocations()
    {
        return allocations;
    }

    public int GetTotalCost()
    {
        int totalCost = 0;
        for (int i = 0; i < supply.Length; i++)
        {
            for (int j = 0; j < demand.Length; j++)
            {
                totalCost += allocations[i, j] * transportationMatrix[i, j];
            }
        }
        return totalCost;
    }

    private bool HasUnallocatedSupplyOrDemand()
    {
        for (int i = 0; i < supply.Length; i++)
        {
            if (supply[i] > 0)
            {
                return true;
            }
        }
        for (int j = 0; j < demand.Length; j++)
        {
            if (demand[j] > 0)
            {
                return true;
            }
        }
        return false;
    }

    private int[] FindLeastCostCell()
    {
        int minCost = int.MaxValue;
        int[] indices = new int[2];

        for (int i = 0; i < supply.Length; i++)
        {
            for (int j = 0; j < demand.Length; j++)
            {
                if (supply[i] > 0 && demand[j] > 0 && transportationMatrix[i, j] < minCost)
                {
                    minCost = transportationMatrix[i, j];
                    indices[0] = i;
                    indices[1] = j;
                }
            }
        }

        return indices;
    }
}

public class Program
{
    public static void Main()
    {
        int[,] transportationMatrix = new int[,]
        {
            { 16, 20, 12},
            { 14, 8, 18},
            { 26, 24, 16}
        };

        int[] supply = new int[] {200, 160, 90};
        int[] demand = new int[] {180, 120, 150};

        TransportationProblemSolver solver = new TransportationProblemSolver(transportationMatrix, supply, demand);
        solver.Solve();

        int[,] allocations = solver.GetAllocations();
        int totalCost = solver.GetTotalCost();

        Console.WriteLine("Allocations:");
        for (int i = 0; i < supply.Length; i++)
        {
            for (int j = 0; j < demand.Length; j++)
            {
                Console.Write("{0}\t", allocations[i, j]);
            }
            Console.WriteLine();
        }

        Console.WriteLine("Total cost: {0}", totalCost);
    }
}
