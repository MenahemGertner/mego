#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#define SIZE 13

int smallLetter(char letter[], int size) {
    int i, counter = 0;
    for (i = 0; i < size; i++) {
        if (letter[i] >= 'a' && letter[i] <= 'z') {
            counter++;
        }
    }
    if (counter == size)
        return 1;
    else
        return 0;
}

int main() {
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
    return 0;
}
