#include <stdio.h>
#include <limits.h>

#define SIZE 5

void main() {
	int arr[SIZE], num, i = 0, a = 0;
	for (i; i < SIZE; i++) {
		printf("Enter a number: ");
		scanf_s("%d", &num);
		arr[i] = num;
		if (arr[i] > a)
			a = arr[i];
	}
	printf("%d", a);
}