#include <stdio.h>

#define SIZE 13

void reverseArray(int arr[], int length) {
    int start = 0, end = length - 1;
    while (start < end) {
        int temp = arr[start];
        arr[start] = arr[end];
        arr[end] = temp;
        start++;
        end--;
    }
}

int main() {
    int arr[] = { 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13};
    reverseArray(arr, SIZE);
    for (int i = 0; i < SIZE; i++) {
        printf("%d ", arr[i]);
    }
    
}
