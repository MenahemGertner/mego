#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include <string.h>
#define LONG 50
#define DRAWN 10

void main() {
	srand(time(NULL));
	char longString[LONG+1]="\0", drawnString[DRAWN+1]="\0";
	int lenRand ,i;
	while ( strlen(longString) <= 50) {
		lenRand = rand() % DRAWN+1;
		for (i = 0; i < lenRand; i++) {
			drawnString[i] = rand() % 26 + 'A';
		}
		if (strlen(longString) + strlen(drawnString) <= 50) {
			strcat_s(longString, drawnString);
			puts(longString);
		}
		else
			break;
	}
	printf("%d", strlen(longString));
	
}