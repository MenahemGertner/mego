#include<stdio.h>
#include<math.h>

// check dividers -> display to screen
void checkDividers(int a, int b);

void main() {

    int num1, num2=0;


    printf("enter a  number: ");
    scanf_s("%d", &num1);

    checkDividers(num1, num2);



}

    // check dividers -> display to screen
    void checkDividers(int a, int b){
        

    //check dividers
        b = a - 1;
        for (; b != 0; b--)
            a *= b;
        
        
            printf("%d\n",a);
        

        


}
