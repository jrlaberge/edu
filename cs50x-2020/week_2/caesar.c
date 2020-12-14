#include <stdio.h>
#include <cs50.h>
#include <string.h>
#include <stdlib.h> // strtol
#include <ctype.h>

void encrypt_text(string plaintext, int key);
int str_to_num(string str_num); // helper function to convert argv[1] to an int. Also handles error checking.

int main(int argc, string argv[])
{
    if (argc != 2 || str_to_num(argv[1]) == 0)
    {
        // We only accept 2 arguments (the program_name + an int), any other argument will throw the usage and exit
        printf("Usage: ./caesar key\n");
        return 1;
    }
    string plaintext = get_string("plaintext: ");
    printf("ciphertext: ");
    encrypt_text(plaintext, str_to_num(argv[1])); // This will print out the ciphertext on the current line.
    printf("\n");
}

void encrypt_text(string plaintext, int key)
{
    if (key > 25)
    {
        // If key is greater than 25 (the length of alphabet (from 0)), then we should get the remainder of key / 26
        key = key % 26;
    }
    // Iterate over the plaintext string char by char.
    for (int i = 0, n = strlen(plaintext); i < n; i++)
    {
        char c = plaintext[i];
        if (islower(c))
        {
            if ((int) c + key <= (int) 'z')
            {
                printf("%c", (int) c + key);
            }
            else
            {
                // if char + key would overflow past Z, then we will revert back to A and count from there.
                printf("%c", (((int) c + key) - (int) 'z' - 1) + (int) 'a');
            }
        }
        else if (isupper(c))
        {
            if ((int) c + key <= (int) 'Z')
            {
                printf("%c", (int) c + key);
            }
            else
            {
                // if char + key would overflow past Z, then we will revert back to A and count from there.
                printf("%c", (((int) c + key) - (int) 'Z' - 1) + (int) 'A');
            }
        }
        else
        {
            // If char is not alpha, then simply print it back.
            printf("%c", plaintext[i]);
        }

    }
}

int str_to_num(string str_num)
{
    char *p;
    int num = 0;

    int errno = 0;
    long conv = strtol(str_num, &p, 10);

    // Check for errors: e.g., the string does not represent an integer
    // or the integer is larger than int
    if (errno != 0 || *p != '\0' || conv > INT_MAX)
    {
        // Put here the handling of the error, like exiting the program with
        // an error message
    }
    else
    {
        // No error
        num = conv;
    }

    return num;
}
