#include <stdio.h>
#include <stdlib.h>
#include <time.h>

#define ROWS 7
#define COLS 5

void overageFunc(int arr1[][COLS], int rows, int cols) {
	int i, j, counter = 0, overage = 0, topOverage = 0, iIndex = 0;
	for (i = 0; i < rows; i++) {
		for (j = 0; j < cols; j++) {
			counter += arr1[i][j];
		}
		overage = counter / cols;
		if (overage > topOverage) {
			topOverage = overage;
			iIndex = i + 1;
		}
		counter = 0;
	}
	printf("The hi overage is the %d student with overage of %d! \n", iIndex, topOverage);
}

void main() {
	srand(time(NULL));
	int arr[ROWS][COLS];
	int i, j, k = rand() % 61 + 40;
	for (i = 0; i < ROWS; i++) {
		for (j = 0; j < COLS; j++) {
			arr[i][j] = k;
			k = rand() % 61 + 40;
		}
	}
	for (i = 0; i < ROWS; i++) {
		for (j = 0; j < COLS; j++) {
			printf("%d ", arr[i][j]);
		}
		printf("\n");
	}
	printf("\n");
	overageFunc(arr, ROWS, COLS);
}