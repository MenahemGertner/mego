# include <stdio.h>


int is_palindrome(int num) {
    int i = num, j = 0;
    for (; i > 0; i /= 10) {
        j *= 10;
        j += i % 10;
    }

    if (num != j) {
        return 0;
    }
    else {
        return 1;
    }
}



void main() {
    int number;

    printf("Enter a number: ");
    scanf_s("%d", &number);

    if (is_palindrome(number)) {
        printf("%s is a palindrome\n", number);
    }
    else {
        printf("%s is not a palindrome\n", number);
    }

}
