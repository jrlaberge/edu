#include <cs50.h>
#include <stdio.h>
#include <math.h>

/*
When making change, odds are you want to minimize the number of coins you’re dispensing for each customer,
lest you run out (or annoy the customer!). Fortunately, computer science has given cashiers everywhere ways
to minimize numbers of coins due: greedy algorithms.

According to the National Institute of Standards and Technology (NIST), a greedy algorithm is one “that always
takes the best immediate, or local, solution while finding an answer. Greedy algorithms find the overall, or
globally, optimal solution for some optimization problems, but may find less-than-optimal solutions for some
instances of other problems.”
*/

int change(float change_owed);

int main(void)
{
    float change_owed = 0.0;
    // change_owed should be a positive float and greater than 0
    do
    {
        change_owed = get_float("Change owed: ");
    }
    while (change_owed <= 0);

    // Display the amount of coins returned the recepient via the change_owed function.
    printf("%i\n", change(change_owed));
}

int change(float dollars)
{
    // Declare the coins we have in the register and their associated value.
    int quarter = 25;
    int dime = 10;
    int nickle = 5;
    int penny = 1;
    int num_coins = 0;
    // Convert the float into a positive int.
    int cents = round(dollars * 100);

    // Iterate over the cents until all change is accounted for.
    do
    {
        if (cents >= quarter)
        {
            num_coins += cents / quarter;
            cents = cents % quarter;
        }
        else if (cents >= dime)
        {
            num_coins += cents / dime;
            cents = cents % dime;
        }
        else if (cents >= nickle)
        {
            num_coins += cents / nickle;
            cents = cents % nickle;
        }
        else if (cents >= penny)
        {
            num_coins += cents / penny;
            cents = cents % penny;
        }
    }
    while (cents > 0);

    // Return an int, containing the number of coins returned.
    return num_coins;
}