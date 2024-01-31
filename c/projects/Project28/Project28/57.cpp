#include <stdio.h>
#include <stdlib.h>
#include <time.h>

#define SIZE 50

void checkLetters(char letters[]) {
	char lostLetters[26] = "\0";
	int i, j, letter, k = 0, m = 0;
	for (j = 0; j < 26; j++) {
		letter = j + 'A';

		for (i = 0; i < SIZE - 1; i++) {
			if (letters[i] == letter) {
				k = 0;
				break;
			}
			else
				k = 1;
		}
		if (k == 1) {
			lostLetters[m] = letter;
			m++;
		}
	}
	puts(lostLetters);
}

void main() {
	srand(time(NULL));
	char arr[SIZE] = "\0";
	int i;
	for (i = 0; i < SIZE - 1; i++) {
		arr[i] = rand() % 26 + 'A';
	}
	puts(arr);
	printf("\n");
	checkLetters(arr);

}
