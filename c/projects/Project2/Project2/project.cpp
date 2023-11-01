#include <stdio.h>

void main() {

	int num, total = 0, counter = 0, average = 0, count = -3;
	while (counter != 3) {
		printf("Enter a number: ");
		scanf_s("%d", &num);
		total += num;
		count += 1;
		if (num == 0)
			counter += 1;

	}
	average = total / count;
	printf("The average is: %d", average);
}