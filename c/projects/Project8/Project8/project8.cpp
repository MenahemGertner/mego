#include <stdio.h>
#include <math.h>

int palindrome(int num) {
    int counter = 0, a = num;
    for (; 0 < a; a /= 10) {
        counter *= 10;
        counter += a % 10;
    }
    return counter;
}

void main() {
    int number;
    printf("Enter a number: ");
    scanf_s("%d", &number);
    if (palindrome(number) == number)
        printf("The number %d is a palindrome", number);
    else
        printf("The number %d is not a palindrome", number);
}
