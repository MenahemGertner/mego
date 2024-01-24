// complex number

#include <stdio.h>


int complex(int num1) {
	int num2 = num1, counter = 0;
	while (num2 != 0) {
		num2--;
		if (num1 % num2 == 0)
			counter += num2;
	}
	if (num1 == counter)
		printf("%d", num1);

}


void main() {
	int num, counter = 1;
	printf("Enter a number: ");
	scanf_s("%d", &num);
	while (counter != num) {
		counter++;
		complex(counter);
	}
}