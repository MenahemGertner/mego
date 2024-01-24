// The most parts

#include <stdio.h>
#include <stdlib.h>
#include <time.h>

int checkMax(int num) {
	int i, counter = 0;
	for (i = num - 1; i == 0; i--) {
		if (num % i == 0)
			counter += 1;
	}
	return counter;
}

void randomNumbers(int max) {
	int number, i, res=0, max_number=0, max_dividtion = 0;
	for (i = 0; i < 10; i++) {
		number = rand() % (max)+1;
		printf("The number %d is: %d", i, number);
		res = checkMax(number);
		if (max_dividtion < res) {
			max_dividtion = res;
			max_number = number;
		}
	}
	printf("The number %d hase %d dividition", max_number, max_dividtion);
}


void main() {
	srand(time(NULL));
	int num;
	printf("Enter a number: ");
	scanf_s("%d", &num);
	randomNumbers(num);
}