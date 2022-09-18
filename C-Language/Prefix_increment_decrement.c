/*P4.3 Prefix increment/decrement*/
#include<stdio.h>
int main(void)
{
	int x=9;
	printf("x=%d\t",x);

    // Prefix increment
	printf("x=%d\t",++x);
	printf("x=%d\t",x);

    // Prefix decrement
	printf("x=%d\t",--x);
	printf("x=%d\n",x);

	return 0;
}
