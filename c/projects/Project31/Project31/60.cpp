#include <stdio.h>
#include <stdlib.h>
#include <time.h>

void mostTime(char numbers[], int len, int* timest, int* theNum) {
	int i, counter, j;
	*timest = 0;
	*theNum = 0;
	for (i = 0; i < 10; i++) {
		counter = 0;
		for (j = 0; j < len; j++) {
			if (i + '0' == numbers[j]) {
				counter += 1;
			}
		}
		if (counter > *timest) {
			*timest = counter;
			*theNum = i;
		}
	}
}

void main() {
	srand(time(NULL));
	int i, theNum = 0, randLong = rand() % 11 + 10, timests = 0;
	char* arr = (char*)malloc(sizeof(char) * randLong + 1);
	for (i = 0; i < randLong; i++) {
		arr[i] = rand() % 10 + '0';
	}
	arr[randLong] = '\0';
	puts(arr);
	mostTime(arr, randLong, &timests, &theNum);
	printf("The number %d appears %d times!", theNum, timests);
	free(arr);
}
