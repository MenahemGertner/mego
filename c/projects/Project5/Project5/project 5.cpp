#include <stdio.h>

void main() {

	int num, counter = 0, min = 9, max = 0, difference;
	printf("Enter a number: ");
	scanf_s("%d", &num);

	while (num > 0) {

		counter += num % 10;
		num /= 10;
		if (counter > max)
			max = counter;
		if (counter < min)
			min = counter;
		counter = 0;
	}
	difference = max - min;
	printf("The difference is: %d", difference);

}