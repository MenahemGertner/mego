#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include <string.h>
#define SIZE 10

void main(){
    srand(time(NULL));
    char arr1[SIZE+1], arr2[SIZE+1];
    int i, randLetter1 = rand() % SIZE+1, randLetter2 = rand() % SIZE+1;

    for (i = 0; i < randLetter1; i++) {
        arr1[i] = rand() % 26 + 'A';
    }
    for (i = 0; i < randLetter2; i++) {
        arr2[i] = rand() % 26 + 'A';
    }

    arr1[randLetter1] = '\0';
    arr2[randLetter2] = '\0';
    puts(arr1);
    puts(arr2);

    if (strlen(arr1) > strlen(arr2)) {
        strcpy_s(arr2, arr1);
    }
    else
    {
        strcpy_s(arr1, arr2);
    }
    printf("\nafter copy:\n\n");
    puts(arr1);
    puts(arr2);
}
