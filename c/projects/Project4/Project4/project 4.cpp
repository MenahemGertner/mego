#include <stdio.h>
#include<limits.h>

void main() {

	int num1, min = 0, max = INT_MAX, num2=0, counter =0;
	printf("Enter a number: ");
	scanf_s("%d", &num1);
	for (; counter < 9; counter += 1) {
		num2 = num1;
		printf("Enter a number: ");
		scanf_s("%d", &num1);
		if (num1 > num2)
			min = num1 - num2;
		else
			min = num2 - num1;
		if (max > min)
			max = min;

	}

	printf("%d", max);
}