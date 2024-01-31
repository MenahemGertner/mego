#include <stdio.h>
#include <stdlib.h>
#include <time.h>

#define SIZE 200

void checkLetters(char letters[]) {
	char lostLetters[26] = "\0";
	int i, j, letter;
	for (j = 0; j < 26; j++) {
		letter = j + 'A';
		for (i = 0; i < SIZE - 1; i++) {
			if (letters[i] == letter) {
				break;
			}
		}
		lostLetters[i] = letter;
	}
	puts(lostLetters);
}

void main() {
	srand(time(NULL));
	char arr[SIZE] = "\0";
	int i;
	for (i = 0; i < SIZE-1; i++) {
		arr[i] = rand() % 26 + 'A';
	}
	puts(arr);
	printf("\n");
	checkLetters(arr);
	
}