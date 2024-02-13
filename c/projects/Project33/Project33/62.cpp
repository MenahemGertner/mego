#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#define SIZE 13

int smallLetter(char letter[], int size) {
	int i, j, counter = 0;
	for (i = 0; i < size; i++) {
		for (j = 0; j < 26; j++) {
			if (j + 'a' == letter[i]) {
				counter++;
				break;
			}
		}
	}
	if (counter == size)
		return 1;
	else
		return 0;
	
}
void main() {
	srand(time(NULL));
	int i;
	char arr[SIZE];
	for (i = 0; i < SIZE; i++) {
		arr[i] = rand() % 26 + 'a';
	}
	arr[SIZE] = '\0';
	if (smallLetter(arr, SIZE))
		printf("Yeeee!!");
	else
		printf("beee!!");
	
}