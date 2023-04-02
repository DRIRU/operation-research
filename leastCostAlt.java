import java.util.Arrays;
import java.util.*;
import java.io.*;

public class leastCost{
    private int[][] transportationMatrix;
    private int[] supply;
    private int[] demand;
    private int numRows;
    private int numCols;
    private int[][] allocations;
    private int totalCost;

    public leastCost(int[][] transportationMatrix, int[] supply, int[] demand, int numRows, int numCols) {
        this.transportationMatrix = transportationMatrix;
        this.supply = supply;
        this.demand = demand;
        this.numRows = numRows;
        this.numCols = numCols;
        this.allocations = new int[numRows][numCols];
        this.totalCost = 0;
    }

    public void solve() {
        while (true) {
            int[] indices = getLeastCostCell();
            int i = indices[0];
            int j = indices[1];
            if (i == -1 || j == -1) {
                break;
            }
            int amount = Math.min(supply[i], demand[j]);
            allocations[i][j] = amount;
            supply[i] -= amount;
            demand[j] -= amount;
        }

        for (int i = 0; i < numRows; i++) {
            for (int j = 0; j < numCols; j++) {
                totalCost += allocations[i][j] * transportationMatrix[i][j];
            }
        }
    }

    private int[] getLeastCostCell() {
        int[] indices = new int[2];
        indices[0] = -1;
        indices[1] = -1;
        int leastCost1 = Integer.MAX_VALUE;

        for (int i = 0; i < numRows; i++) {
            for (int j = 0; j < numCols; j++) {
                if (supply[i] > 0 && demand[j] > 0 && transportationMatrix[i][j] < leastCost1) {
                    indices[0] = i;
                    indices[1] = j;
                    leastCost1 = transportationMatrix[i][j];
                }
            }
        }

        return indices;
    }

    public int[][] getAllocations() {
        return allocations;
    }

    public int getTotalCost() {
        return totalCost;
    }
    public static void main(String[] args) {
        int[][] transportationMatrix = {{1,2},{3,4}};
        int[] supply = {5,6};
        int[] demand = {7,4};
        int numRows = 2;
        int numCols = 2;

        leastCost solver = new leastCost(transportationMatrix, supply, demand, numRows, numCols);
        solver.solve();

        int[][] allocations = solver.getAllocations();
        int totalCost = solver.getTotalCost();

        System.out.println("Sol is "+ totalCost);
    }
}
