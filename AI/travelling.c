#include <stdio.h>

int ary[10][10], completed[10], n, cost = 0, minCost = 999;

void takeInput() {
    int i, j;
    printf("Enter the number of nodes: ");
    scanf("%d", &n);
    printf("\nEnter the Cost Matrix\n");
    for (i = 0; i < n; i++) {
        for (j = 0; j < n; j++)
            scanf("%d", &ary[i][j]);
        completed[i] = 0;
    }
}

void tsp(int city, int count) {
    int i;
    completed[city] = 1;

    if (count == n) {
        if (ary[city][0] + cost < minCost) {
            minCost = ary[city][0] + cost;
        }
    }

    for (i = 0; i < n; i++) {
        if (!completed[i] && ary[city][i] != 0) {
            cost += ary[city][i];
            tsp(i, count + 1);
            cost -= ary[city][i];
        }
    }

    completed[city] = 0;
}

int main() {
    takeInput();
    printf("\n\nThe path is: \n");
    tsp(0, 1); // Start from city 0, and we have visited 1 city so far
    printf("\n\nMinimum cost is %d\n", minCost);
    return 0;
}
