#include<stdio.h>
#include<math.h>

int polendrom(int num) {
	
	int counter = 0;
	for (; 0 < num; counter *= 10)
		counter += num % 10;
		num /= 10;
		
		
	
	return counter;
}

void main() {

	int number;
	printf("Enter a number: ");
	scanf_s("%d", & number);
	if (polendrom(number) == number)
		printf("The number %d is polendrom", number);
	else
		printf("The number %d is not polendrom", number);

}