#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#define SIZE 7

void main() {
	srand(time(NULL));
	int arr[SIZE] = {1, 2, 3, 4, 5, 6, 7};
	int* ptr = &arr[rand() % SIZE];
	
	printf("%d", *ptr);

}