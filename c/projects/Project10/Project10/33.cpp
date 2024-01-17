// 1089

#include <stdio.h>

int opposite_number(int num1) {
	int num2 = 0, i;
	for (i = 0; i < 3; i++) {
		num2 *= 10;
		num2 += num1 % 10;
		num1 /= 10;
	}
	return num2;
}

int reduction(int num1, int num2) {
	int res = 0;
	if (num1 > num2)
		res = num1 - num2;
	else
		res = num2 - num1;
	return res;
}

void main() {
	int num, res = 0, small_num = 0, larg_num = 0;

	printf("Enter a number: ");
	scanf_s("%d", &num);
	res = opposite_number(num);
	small_num = reduction(res, num);
	larg_num = opposite_number(small_num);
	res = larg_num + small_num;
	printf("%d", res);


}