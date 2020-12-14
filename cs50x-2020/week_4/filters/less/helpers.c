#include "helpers.h"
#include <math.h>

// Convert image to grayscale
void grayscale(int height, int width, RGBTRIPLE image[height][width])
{
    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
        {
            int r = image[i][j].rgbtRed;
            int g = image[i][j].rgbtGreen;
            int b =image[i][j].rgbtBlue;
            float avgr = (float)(r + g + b) / 3;
            int avg = round(avgr);
            // set avg for rgb values
            image[i][j].rgbtRed = avg;
            image[i][j].rgbtGreen = avg;
            image[i][j].rgbtBlue = avg;
        }
    }
    return;
}

// Convert image to sepia
void sepia(int height, int width, RGBTRIPLE image[height][width])
{
    // Formula for Sepia
    //outputRed = (inputRed * .393) + (inputGreen *.769) + (inputBlue * .189)
    //outputGreen = (inputRed * .349) + (inputGreen *.686) + (inputBlue * .168)
    //outputBlue = (inputRed * .272) + (inputGreen *.534) + (inputBlue * .131)
    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
        {
            // use sepia algorithim
            float sr = (float) .393 * image[i][j].rgbtRed + .769 * image[i][j].rgbtGreen + .189 * image[i][j].rgbtBlue;
            float sg = (float) .349 * image[i][j].rgbtRed + .686 * image[i][j].rgbtGreen + .168 * image[i][j].rgbtBlue;
            float sb = (float) .272 * image[i][j].rgbtRed + .534 * image[i][j].rgbtGreen + .131 * image[i][j].rgbtBlue;
            // round values
            int rsr = round(sr);
            int rsg = round(sg);
            int rsb = round(sb);
            // make sure it doesnt go over 255
            if (rsr > 255)
            {
                rsr = 255;
            }
            if (rsg > 255)
            {
                rsg = 255;
            }
            if (rsb > 255)
            {
                rsb = 255;
            }
            // set values as rgb values
            image[i][j].rgbtRed = rsr;
            image[i][j].rgbtGreen = rsg;
            image[i][j].rgbtBlue = rsb;
        }
    }
    return;
}

// Reflect image horizontally
void reflect(int height, int width, RGBTRIPLE image[height][width])
{
    RGBTRIPLE new_image[height][width];
    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
        {
            new_image[i][j] = image[i][width - j - 1];
        }
    }
    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
        {
            image[i][j] = new_image[i][j];
        }
    }
    return;
}

void blur(int height, int width, RGBTRIPLE image[height][width])
{
    RGBTRIPLE ogImage[height][width];
    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
        {
            ogImage[i][j] = image[i][j];
        }
    }

    for (int i = 0, red, green, blue, counter; i < height; i++)
    {
        for (int j = 0; j < width; j++)
        {
            red = green = blue = counter = 0;

            if (i >= 0 && j >= 0)
            {
                red += ogImage[i][j].rgbtRed;
                green += ogImage[i][j].rgbtGreen;
                blue += ogImage[i][j].rgbtBlue;
                counter++;
            }
            if (i >= 0 && j - 1 >= 0)
            {
                red += ogImage[i][j-1].rgbtRed;
                green += ogImage[i][j-1].rgbtGreen;
                blue += ogImage[i][j-1].rgbtBlue;
                counter++;
            }
            if ((i >= 0 && j + 1 >= 0) && (i >= 0 && j + 1 < width))
            {
                red += ogImage[i][j+1].rgbtRed;
                green += ogImage[i][j+1].rgbtGreen;
                blue += ogImage[i][j+1].rgbtBlue;
                counter++;
            }
            if (i - 1 >= 0 && j >= 0)
            {
                red += ogImage[i-1][j].rgbtRed;
                green += ogImage[i-1][j].rgbtGreen;
                blue += ogImage[i-1][j].rgbtBlue;
                counter++;
            }
            if (i - 1 >= 0 && j - 1 >= 0)
            {
                red += ogImage[i-1][j-1].rgbtRed;
                green += ogImage[i-1][j-1].rgbtGreen;
                blue += ogImage[i-1][j-1].rgbtBlue;
                counter++;
            }
            if ((i - 1 >= 0 && j + 1 >= 0) && (i - 1 >= 0 && j + 1 < width))
            {
                red += ogImage[i-1][j+1].rgbtRed;
                green += ogImage[i-1][j+1].rgbtGreen;
                blue += ogImage[i-1][j+1].rgbtBlue;
                counter++;
            }
            if ((i + 1 >= 0 && j >= 0) && (i + 1 < height && j >= 0))
            {
                red += ogImage[i+1][j].rgbtRed;
                green += ogImage[i+1][j].rgbtGreen;
                blue += ogImage[i+1][j].rgbtBlue;
                counter++;
            }
            if ((i + 1 >= 0 && j - 1 >= 0) && (i + 1 < height && j - 1 >= 0))
            {
                red += ogImage[i+1][j-1].rgbtRed;
                green += ogImage[i+1][j-1].rgbtGreen;
                blue += ogImage[i+1][j-1].rgbtBlue;
                counter++;
            }
            if ((i + 1 >= 0 && j + 1 >= 0) && (i + 1 < height && j + 1 < width))
            {
                red += ogImage[i+1][j+1].rgbtRed;
                green += ogImage[i+1][j+1].rgbtGreen;
                blue += ogImage[i+1][j+1].rgbtBlue;
                counter++;
            }

            image[i][j].rgbtRed = round(red / (counter * 1.0));
            image[i][j].rgbtGreen = round(green / (counter * 1.0));
            image[i][j].rgbtBlue = round(blue / (counter * 1.0));
        }
    }

    return;
}
