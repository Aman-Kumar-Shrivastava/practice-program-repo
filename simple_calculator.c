#include <stdio.h>
#include <math.h>

void menu() {
    printf("\n===== Simple Calculator =====\n");
    printf("1. Addition\n");
    printf("2. Subtraction\n");
    printf("3. Multiplication\n");
    printf("4. Division\n");
    printf("5. Modulus\n");
    printf("6. Power\n");
    printf("7. Exit\n");
    printf("Choose an operation (1-7): ");
}

int main() {
    int choice;
    double first, second, result;

    while (1) {
        menu();
        scanf("%d", &choice);

        if (choice == 7) {
            printf("Exiting calculator... Goodbye!\n");
            break;
        }

        printf("Enter first number: ");
        scanf("%lf", &first);
        printf("Enter second number: ");
        scanf("%lf", &second);

        switch (choice) {
            case 1:
                result = first + second;
                printf("Result = %.2lf\n", result);
                break;
            case 2:
                result = first - second;
                printf("Result = %.2lf\n", result);
                break;
            case 3:
                result = first * second;
                printf("Result = %.2lf\n", result);
                break;
            case 4:
                if (second != 0)
                    result = first / second;
                else {
                    printf("Error! Division by zero.\n");
                    continue;
                }
                printf("Result = %.2lf\n", result);
                break;
            case 5:
                printf("Result = %d\n", (int)first % (int)second);
                break;
            case 6:
                result = pow(first, second);
                printf("Result = %.2lf\n", result);
                break;
            default:
                printf("Invalid input! Please try again.\n");
        }
    }

    printf("Developed by: Aman\n");
    return 0;
}
