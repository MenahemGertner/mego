#include <stdio.h>
#include <string.h>
#define SIZE 20


void main() {
	char arr1[SIZE] ="\0", arr2[SIZE]="\0";
	int i;
	for (i = 0; i < 5; i++) {
		printf("Enter a string.. ");
		gets_s(arr1);
		if (strlen(arr1) > strlen(arr2)) {
			strcpy_s(arr2, arr1);
		}
	}
	printf("\nThe longest string is '%s'", arr2);
}