#include <stdio.h>

int main()
{
    /*Variable declaration*/
    int a, b;

    /*Initializing loop and printing the table*/
    for (a = 1; a <= 10; a++)
    {
        for (b = a; b <= 10; b++)
        {
            printf("%3d", b);
        }
        printf("\n");
    }
}
