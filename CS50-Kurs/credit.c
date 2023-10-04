#include <cs50.h>
#include <stdio.h>

int main(void)
{
    // get card number
    long number = get_long("Number: ");

    int lastdigit = 0;
    int digits = 0;
    int sum1 = 0;
    int sum2 = 0;
    int div1;
    int div2;
    int sumall;
    long start = number;

    // how long
    while (number > 0)
    {
        div1 = number % 10;
        sum1 += div1;
        number = number / 10;
        digits++;
        if (number > 0)
        {
            div2 = (number % 10) * 2;
            int firstdigit;
            int seconddigit;
            int sum3 = 0;
            if (div2 > 9)
            {
                seconddigit = div2 % 10;
                firstdigit = div2 / 10;
                sum3 = firstdigit + seconddigit;
                div2 = sum3;
            }
            sum2 += div2;
            number = number / 10;
            digits++;
        }
    }

    //sum of both things
    sumall = (sum1 + sum2) % 10;

    //if it invalid
    if ((digits != 13 && digits != 15 && digits != 16) || sumall != 0)
    {
        printf("INVALID\n");
        return 0;
    }

    //which type
    do
    {
        start = start / 10;
    }
    while (start > 100);

    if ((start / 10 == 5) && (0 < start % 10 && start % 10 < 6))
    {
        printf("MASTERCARD\n");
    }
    else if ((start / 10 == 3) && (start % 10 == 4 || start % 10 == 7))
    {
        printf("AMEX\n");
    }
    else if (start / 10 == 4)
    {
        printf("VISA\n");
    }
    // invalid if doesnt start with right digit
    else
    {
        printf("INVALID\n");
    }
}