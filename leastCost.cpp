#include <iostream>
#include <climits>

using namespace std;

class TransportationProblemSolver {
    private:
        int** transportationMatrix;
        int* supply;
        int* demand;
        int** allocations;
        int numRows;
        int numCols;

    public:
        TransportationProblemSolver(int** transportationMatrix, int* supply, int* demand, int numRows, int numCols) {
            this->transportationMatrix = transportationMatrix;
            this->supply = supply;
            this->demand = demand;
            this->numRows = numRows;
            this->numCols = numCols;
            this->allocations = new int*[numRows];
            for (int i = 0; i < numRows; i++) {
                this->allocations[i] = new int[numCols]();
            }
        }

        void solve() {
            while (hasUnallocatedSupplyOrDemand()) {
                int* indices = findLeastCostCell();
                int supplyIndex = indices[0];
                int demandIndex = indices[1];

                int allocation = min(supply[supplyIndex], demand[demandIndex]);
                allocations[supplyIndex][demandIndex] = allocation;

                supply[supplyIndex] -= allocation;
                demand[demandIndex] -= allocation;

                delete[] indices;
            }
        }

        int** getAllocations() {
            return allocations;
        }

        int getTotalCost() {
            int totalCost = 0;
            for (int i = 0; i < numRows; i++) {
                for (int j = 0; j < numCols; j++) {
                    totalCost += allocations[i][j] * transportationMatrix[i][j];
                }
            }
            return totalCost;
        }

    private:
        bool hasUnallocatedSupplyOrDemand() {
            for (int i = 0; i < numRows; i++) {
                if (supply[i] > 0) {
                    return true;
                }
            }
            for (int j = 0; j < numCols; j++) {
                if (demand[j] > 0) {
                    return true;
                }
            }
            return false;
        }

        int* findLeastCostCell() {
            int minCost = INT_MAX;
            int* indices = new int[2];

            for (int i = 0; i < numRows; i++) {
                for (int j = 0; j < numCols; j++) {
                    if (supply[i] > 0 && demand[j] > 0 && transportationMatrix[i][j] < minCost) {
                        minCost = transportationMatrix[i][j];
                        indices[0] = i;
                        indices[1] = j;
                    }
                }
            }

            return indices;
        }
};

int main() {
    int numRows, numCols;
    cout<<"Enter No. of Suppliers and Destinations: ";
    cin>>numRows>>numCols;
    int* supply = new int[numRows];
    cout<<"Enter Supply values: ";
    for(int i = 0; i<numRows; i++)
        cin>>supply[i];
    int* demand = new int[numCols];
    cout<<"Enter demand values: ";
    for(int i = 0; i<numCols; i++)
        cin>>demand[i];
    int** transportationMatrix = new int*[numRows];
    cout<<"Enter the costs: \n";
    for(int i = 0; i < numRows; i++) 
    {
        transportationMatrix[i] = new int[numCols];
        for(int j = 0; j<numCols; j++)
            cin>>transportationMatrix[i][j];
    }
    TransportationProblemSolver solver(transportationMatrix, supply, demand, numRows, numCols);
    solver.solve();

    int** allocations = solver.getAllocations();
    int totalCost = solver.getTotalCost();

    cout << "Allocations:\n";
    for (int i = 0; i < numRows; i++) {
        for (int j = 0; j < numCols; j++) {
            cout << allocations[i][j] << " ";
        }
        cout << endl;
    }
    cout << "Total Cost: " << totalCost << endl;

    for (int i = 0; i < numRows; i++) {
        delete[] transportationMatrix[i];
        delete[] allocations[i];
    }
    delete[] transportationMatrix;
    delete[] allocations;
    delete[] supply;
    delete[] demand;

    return 0;
}

   
