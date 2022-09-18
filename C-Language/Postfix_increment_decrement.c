/*P4.4 Program to understand the use of postfix increment/decrement*/
#include<stdio.h>
int main()
{
	int x=8;
	printf("x=%d\t",x);

    // Postfix increment
	printf("x=%d\t",x++);
	printf("x=%d\t",x);

    // Postfix decrement
	printf("x=%d\t",x--);
	printf("x=%d\n",x);

	return 0;
}
