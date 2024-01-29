#include <stdio.h>
#include <stdlib.h>
#include <time.h>

#define ROWS 10
#define COLS 10

void main() {
	srand(time(NULL));
	int arr[ROWS][COLS], i, j, k = rand()%8 + 1;
	for (i = 0; i < ROWS; i++) {
		for (j = 0; j < COLS; j++) {
			arr[i][j] = k;
			k = rand() % 8+1;
			printf("%d ", arr[i][j]);
		}
		printf("\n");
	}

}