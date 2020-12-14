#include <cs50.h>
#include <stdio.h>
#include <stdlib.h>

void verify_card(long card_num);
int len(long n);

int main(void)
{
    long card_num = get_long("Number: ");
    verify_card(card_num);
}

void verify_card(long card_num)
{
    long digits = card_num; // store a separate copy of card_num to preserve card_num
    int odd = 0;
    int odd_product;
    int even = 0;
    int first_digit; // will store the first digit to check card_type
    int second_digit; // will store the second digit to check card_type

    for (int i = 0; i < len(card_num); i++)
    {
        int n = digits % 10;
        digits /= 10;
        /* Luhn's Algorithm
            1. Multiply every other digit by 2, starting with the number’s second-to-last digit, and then add those products’ digits together.
            2. Add the sum to the sum of the digits that weren’t multiplied by 2.
            3. If the total’s last digit is 0 (or, put more formally, if the total modulo 10 is congruent to 0), the number is valid!
        */
        if (i % 2 == 0)
        {
            even = even + n;
        }
        else
        {
            odd_product = n * 2;
            // For odd products, we want the digits themselves, so we will split them.
            for (int j = 0; j <= len(odd_product); j++)
            {
                odd = odd + (odd_product % 10);
                odd_product /= 10;
            }
        }
        // get second digit
        if (i + 2 == len(card_num))
        {
            second_digit = n;
        }
        // get first digit
        if (i + 1 == len(card_num))
        {
            first_digit = n;
        }

    }
    if ((odd + even) % 10 == 0)
    {
        // Visa can be 13 or 16 digits, and always start with 4
        if ((len(card_num) == 13 || len(card_num) == 16) && first_digit == 4)
        {
            printf("VISA\n");
        }
        // Amex is always 15 digits and can start with 34 or 37
        else if (len(card_num) ==  15 && first_digit == 3 && (second_digit == 4 || second_digit == 7))
        {
            printf("AMEX\n");
        }
        // Mastercard is always 16 digits and can start between 51 and 55 (inclusive)
        else if (len(card_num) == 16 && first_digit == 5 && (second_digit >= 1 && second_digit <= 5))
        {
            printf("MASTERCARD\n");
        }
        // We do not support types other than those listed above, so anything else is considered INVALID.
        else
        {
            printf("INVALID\n");
        }
    }
    // If checksum (Using Luhn's algorithm) fails, we can assume the card is invalid.
    else
    {
        printf("INVALID\n");
    }
}

int len(long num)
{
    // helper function to calculate the length of a long number.
    int length = 1;
    while (num > 9)
    {
        length++;
        num /= 10;
    }
    return length;
}