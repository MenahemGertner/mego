#include <stdio.h>
#include <string.h>
#define SIZE 10

int polendrom(char num[]) {
	int i, n =0, m, newNum = 0;
	puts(num);
	for (i = 0; i < strlen(num); i++) {
		n *= 10;
		n += num[i];
	}
	m = n;

	for (i = 0; i < strlen(num); i++){
		newNum *= 10;
		newNum += m % 10;
		m /= 10;
	}
	if (n == newNum)
		return 1;
	else
		return 0;
}

void main() {
	char arr[SIZE] = {1,2,3,2,1};
	
	if (polendrom(arr))
		printf("This number is polendrom!");
	else
		printf("This number is not polendrom!");
}