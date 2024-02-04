#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#define SIZE 200

void repeatingLetter(char letters[], int size) {
	int i, j, counter, letter, lettetTimes = 0, letterRepeat = 0;
	for (i = 0; i < 26; i++) {		
		counter = 0;
		letter = i + 'A';
		for (j = 0; j < size; j++) {
			if (letter == letters[j])
				counter++;
		}
		if (counter > lettetTimes) {
			lettetTimes = counter;
			letterRepeat = letter;
		}
	}
	printf("%d, %c", lettetTimes, letterRepeat);
}

void main() {
	srand(time(NULL));
	char arr[SIZE+1] = "\0";
	int i;
	for (i = 0; i < SIZE; i++) {
		arr[i] = rand() % 26 + 'A';
	}
	puts(arr);
	printf("\n");
	repeatingLetter(arr, SIZE);
}