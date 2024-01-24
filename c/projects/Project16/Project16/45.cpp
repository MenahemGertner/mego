#include<stdio.h>
#include<stdlib.h>
#include<time.h>


#define ROWS 5
#define COLS 5

// 2D array with function
void slant(int arr2[][COLS], int rows, int cols) {
    int i, j=0;
    for (i = 0; i < rows; i++, j++) {
        printf("%d, ", arr2[i][j]);
    }
    printf("\n\n");
    j = 4;
    for (i = 0; i < rows; i++, j--) {
        printf("%d, ", arr2[i][j]);
    }

}
void display2D(int arr[][COLS], int rows, int cols) {
    int i, j, k = rand() % 100;

    for (i = 0; i < rows; i++)
        for (j = 0; j < cols; j++) {

            arr[i][j] = k;
            k = rand() % 100;
        }


    for (i = 0; i < rows; i++) {
        for (j = 0; j < cols; j++) {
            printf("%d  ", arr[i][j]);
        }

        printf("\n");

    }
    printf("\n\n");

    
    slant(arr, rows, cols);
    printf("\n\n");

}

void main() {
    srand(time(NULL));

    int arr1[ROWS][COLS];
    
    display2D(arr1, ROWS, COLS);


    }


