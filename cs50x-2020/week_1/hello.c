#include <cs50.h>
#include <stdio.h>

int main(void)
{
    // Ask for user's name.
    string name = get_string("Hi, what is your name? ");
    //Concatenate User's name with Hello
    printf("Hello, %s\n", name);
}