#include <cs50.h>
#include <stdio.h>

int main(void)
{
    int n;
    do
    {
        n = get_int("Height: ");
    }
    while(n<1 || n>8);

//for euch row
    for(int i = 0; i < n; i++)
    {
        for(int j = 0; j < n - i - 1; j++)
    {
        // print a space
        printf(" ");
    }
    // print a brick
    for(int s = 0; s <= i; s++)
    {
        printf("#");
    }

    {
    for(int jj = n-2; jj < n; jj++)
    {
        printf(" ");
    }
    for(int ss = 0; ss <= i; ss++)
    {
        printf("#");
    }
    }
    //move to next row
    printf("\n");
    }
}