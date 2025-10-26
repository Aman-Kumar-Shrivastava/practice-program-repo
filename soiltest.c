#include<stdio.h>
#include<stdlib.h>

//declaration
void Wavelength();
void TabularChart();

int  main ()
{   int choice;
    printf("1.value of wavelength (in nm)\n"); 
    printf("2.Tabular chart of the wavelenght\n");
    printf("3.Exit\n");
    printf ("Enter a valind choice (1-3)\n");
    scanf ("%d", &choice);

  
    switch (choice) {
        case 1:
        Wavelength();
        break;
        
        case 2:
        TabularChart();
        break;
        
        case 3:
        exit(0);
        break;
        
        default: ("please enter a valid value\n");
        break;
}
return 0;
}
    
    
void Wavelength() {
    printf("Enter the wavelength (in nm)\n");
    int wavelength;
    scanf("%d", &wavelength);

    
        if(wavelength >= 400 && wavelength < 500) {
        printf("Wavelength: %d nm\n", wavelength);
        printf("Condition: Low organic matter\n");
        printf("Suggestion: Add compost\n");
    } 
    else if (wavelength >= 500 && wavelength < 600) {
        printf("Wavelength: %d nm\n", wavelength);
        printf("Condition: Nitrogen deficient\n");
        printf("Suggestion: Add urea or ammonium nitrate\n");
    } 
    else if (wavelength >= 600 && wavelength < 700) {
        printf("Wavelength: %d nm\n", wavelength);
        printf("Condition: Phosphorus deficient\n");
        printf("Suggestion: Add superphosphate\n");
    } 
    else if (wavelength >= 700 && wavelength < 800) {
        printf("Wavelength: %d nm\n", wavelength);
        printf("Condition: Potassium deficient\n");
        printf("Suggestion: Add muriate of potash\n");
    } 
    else if (wavelength >= 800 && wavelength <= 900) {
        printf("Wavelength: %d nm\n", wavelength);
        printf("Condition: Low fertility overall\n");
        printf("Suggestion: Add compost + NPK fertilizer\n");
    } 
    else {
        printf("Wavelength: %d nm\n", wavelength);
        printf("Out of range! Please enter a value between 400–900 nm.\n");
    }
}

void TabularChart() {
    printf("Wavelength (nm) | Condition               | Suggestion\n");
    printf("-------------------------------------------------------\n");
    printf("400-499         | Low organic matter      | Add compost\n");
    printf("500-599         | Nitrogen deficient      | Add urea or ammonium nitrate\n");
    printf("600-699         | Phosphorus deficient    | Add superphosphate\n");
    printf("700-799         | Potassium deficient     | Add muriate of potash\n");
    printf("800-900         | Low fertility overall   | Add compost + NPK fertilizer\n");
}
 