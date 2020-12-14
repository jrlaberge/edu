#include <cs50.h>
#include <stdio.h>

void print_pyramid(int height);
void print_blocks(int n);
void print_spaces(int n);

int main(void)
{
    int height;
    do
    {
        height = get_int("Height: ");
    }
    // Only accept input that is between (inclusive) 1 and 8
    while (height < 1 || height > 8);
    print_pyramid(height);
}

void print_pyramid(int height)
{
    // We start at 1, since we do not accept 0 for the blocks.
    for (int i = 1; i <= height; i++)
    {
        // height - i will properly pad the spaces
        print_spaces(height - i);
        print_blocks(i);
        // Padding between the blocks.
        printf("  ");
        print_blocks(i);
        printf("\n");
    }
}

void print_blocks(int n)
{
    // Print the number of blocks required.
    for (int i = 0; i < n; i++)
    {
        printf("#");
    }
}

void print_spaces(int n)
{
    // Print the spacing preceding the blocks.
    for (int i = 0; i < n; i++)
    {
        printf(" ");
    }
}