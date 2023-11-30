#include <stdio.h>
#include <math.h>


long getFactorial(int num) {

	long result = 1;
	int i;

	for (i = 1; i <= num; i++)
		result *= i;

	return result;

}

	void main(){

		int number;
		long my_result;

		printf("Enter a number: ");
		scanf_s("%d", &number);

		my_result = getFactorial(number);
		printf("The factorial of %d is %d", number, my_result);



}