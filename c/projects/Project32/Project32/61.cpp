#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include <string.h>

void main() {
	srand(time(NULL));
	int num1, num2, i;
	printf("Enter a number: ");
	scanf_s("%d", &num1);
	printf("Enter a number: ");
	scanf_s("%d", &num2);
	char* arr1 = (char*)malloc(sizeof(char) * num1 + 1);
	char* arr2 = (char*)malloc(sizeof(char) * num2 + 1);
	for (i = 0; i < num1; i++) {
		arr1[i] = rand() % 26 + 'a';
	}

	arr1[num1] = '\0';
	for (i = 0; i < num2; i++) {
		arr2[i] = rand() % 26 + 'a';
	}
	arr2[num2] = '\0';

	puts(arr1);
	puts(arr2);
	char* longArr = (char*)malloc(sizeof(char) * (num1 + num2) + 3);

	longArr[num1 + num2 + 2] = '\0';
	if (num1 > num2) {
		strcat(longArr, arr2);
		strcat(longArr, arr1);
	}
	else {
		strcat(longArr, arr1);
		strcat(longArr, arr2);
	}
	puts(longArr);

	free(arr1);
	free(arr2);
	free(longArr);

}