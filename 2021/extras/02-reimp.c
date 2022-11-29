// https://adventofcode.com/2021/day/2
// Solved in Python then reimplemented in C

#include <stdio.h>
#include <string.h>

//#define INPUTFILE "testdata.txt"
//#define INPUTLEN 6
#define INPUTFILE "../02data.txt"
#define INPUTLEN 1000

int main(void) {
    FILE *fptr;
    if ((fptr = fopen(INPUTFILE, "r")) == NULL) {
        printf("Error opening file\n");
       return 1;
    }
    char command[INPUTLEN][8];
    int quantity[INPUTLEN];
    for (int line = 0; line < INPUTLEN; line++) {
        fscanf(fptr, "%s", command[line]);
        fscanf(fptr, "%d", &quantity[line]);
    }
    fclose(fptr);

    // Part 1
    int horizontal = 0;
    int depth = 0;
    for (int n = 0; n < INPUTLEN; n++) {
        if (!strcmp(command[n], "forward")) {
            horizontal = horizontal + quantity[n];
        } else if (!strcmp(command[n], "down")) {
            depth = depth + quantity[n];
        } else if (!strcmp(command[n], "up")) {
            depth = depth - quantity[n];
        } else {
            printf("Error unexpected string\n");
            return 1;
        }
    }
    printf("%d\n", horizontal * depth);

    // Part 2
    horizontal = 0;
    depth = 0;
    int aim = 0;
    for (int n = 0; n < INPUTLEN; n++) {
        if (!strcmp(command[n], "forward")) {
            horizontal = horizontal + quantity[n];
            depth = depth + aim * quantity[n];
        } else if (!strcmp(command[n], "down")) {
            aim = aim + quantity[n];
        } else if (!strcmp(command[n], "up")) {
            aim = aim - quantity[n];
        } else {
            printf("Error unexpected string\n");
            return 1;
        }
    }
    printf("%d\n", horizontal * depth);

    return 0;
}
