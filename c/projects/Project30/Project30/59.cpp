#include <stdio.h>
#include <stdlib.h>


void main() {
	int num, i;
	printf("Enter a number: ");
	scanf_s("%d", &num);
	char* arr;
	arr = (char*)malloc(sizeof(char) * num+1);
	
	
	for (i = 0; i < num; i++) {
		printf("Enter a string: ");
		scanf_s(" %c", &arr[i]);
	}
	arr[num] = '\0';
	puts(arr);
	free(arr);
}

