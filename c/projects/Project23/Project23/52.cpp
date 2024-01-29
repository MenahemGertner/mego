#include<stdio.h>
#define SIZE 3

void main() {
	int i, j, arr[SIZE][SIZE] = { {1, 2, 3}, {4, 5, 6}, {7, 8, 9} };
	int* ptr = &arr[0][0];
	
	for (i = 0; i < SIZE * SIZE; i++) {
			printf("%d", *ptr++);
	}
}