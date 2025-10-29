#include <stdio.h>
#include <stdlib.h>
#include <time.h>

int main()
{
    int random, guess;
    int attempts = 0;

    srand(time(NULL));  // Seed random number generator

    printf("Welcome to the guessing game!\n");

    random = rand() % 100 + 1;  // Generate number between 1–100

    do {
        printf("Enter your guess number between 1 to 100: ");
        scanf("%d", &guess);
        attempts++;

        if (guess < random)
            printf("Guess a larger number.\n");
        else if (guess > random)
            printf("Guess a smaller number.\n");
        else
            printf("🎉 Congratulations! You guessed the number in %d attempts!\n", attempts);

    } while (random != guess);

    printf("Game ended. Thanks for playing!\n");
    printf("Developed by: Aman\n");

    return 0;
}
