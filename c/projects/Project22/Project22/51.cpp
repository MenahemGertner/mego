#include<stdio.h>
#include<string.h>

void main() {

    char myName[] = "menahem gertner";
    char* ptr = &myName[0];
    int len = strlen(myName);

    for (len; len > 0; len--) {
        printf("%c", *ptr++);
    }

}
