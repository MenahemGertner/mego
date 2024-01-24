#include <stdio.h>

#define SIZE 5

void main() {
	int arr[SIZE], num, i = 0;
	for (i; i < SIZE; i++) {
		printf("Enter a number: ");
		scanf_s("%d", &num);
		arr[i] = num;
	}
	printf("%d", arr);
}