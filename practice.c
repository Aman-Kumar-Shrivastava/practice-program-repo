#include<stdio.h>
int main() {
    
    typedef struct pokemon {
        char name[50];
        int hp;
        int speed;
        int attack;
    } Pokemon;

    Pokemon arr[10];

    for(int i = 0; i < 3; i++) {
        printf("Enter nameof pokemon %d:\n", i + 1);
        scanf("%s", arr[i].name);
        printf("Enter hp of pokemon %d:\n", i + 1);
        scanf("%d", &arr[i].hp);    
        printf("Enter speed of pokemon %d:\n", i + 1);
        scanf("%d", &arr[i].speed);
        printf("Enter attack of pokemon %d:\n", i + 1);
        scanf("%d", &arr[i].attack);

    }
    for (int i = 0; i < 3; i++) {
        printf("Details of pokemon %d:\n", i + 1);
        printf("Name: %s\n", arr[i].name);
        printf("HP: %d\n", arr[i].hp);
        printf("Speed: %d\n", arr[i].speed);
        printf("Attack: %d\n", arr[i].attack);
    }
    return 0;
}