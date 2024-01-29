#include<stdio.h> 
#define SIZE 7

void main() {

    int arr[SIZE] = { 1,2,3,4,5,6,7 };
    //int array[SIZE];
    int i = 0;

    int* ptr;
    ptr = &arr[SIZE -1]; // ptr=arr;


    for (i = 0; i < SIZE; i++) {
        
        printf("%d  ", *ptr--);

    }

}
