// Goldbach hypothesis

#include <stdio.h>

int primeNumber(int num1) {
	int i = num1;
	for (i; i != 0;) {
		i--;
		if (num1 % i == 0)
			return false;
	}
	return true;
}

int checkingTheSum(int num1) {
	int num2 = num1 / 2, num3 = 0;
	while (num2 != num1) {
		if (primeNumber(num2)) {
			num3 = num1 - num2;
			if (primeNumber(num3)) 
				return true;
		}
		num2 += 1;
	}
	return false;
}

int goOverNumbers(int number) {
	int counter = 2;
	while (counter != number) {
		if (checkingTheSum(counter))
			counter += 2;
		else
			return false;
	}
	return true;
}


void main() {
	int num;
	printf("Enter a number: ");
	scanf_s("%d", &num);
	if (goOverNumbers(num))
		printf("The Goldbach hypothesis is true!");
	else
		printf("The Goldbach hypothesis is false!");
}