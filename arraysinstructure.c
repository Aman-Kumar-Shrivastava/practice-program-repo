#include<stdio.h>
#include<string.h>
#include<stdbool.h>
struct person {
    char name[50];
    int salary;
    int age;
};
int main() {
    struct person arr[5];
    for(int i = 0; i < 3; i++) {
        printf("Enter name of person %d:\n", i + 1);
        scanf("%s", arr[i].name);
        printf("Enter salary of person %d:\n", i + 1);
        scanf("%d", &arr[i].salary);    
        printf("Enter age of person %d:\n", i + 1);
        scanf("%d", &arr[i].age);
    }
    for (int i = 0; i < 3; i++) {
        printf("Details of person %d:\n", i + 1);
        printf("Name: %s\n", arr[i].name);
        printf("Salary: %d\n", arr[i].salary);
        printf("Age: %d\n", arr[i].age);
    }
    return 0;
}