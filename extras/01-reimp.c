// https://adventofcode.com/2021/day/1
// Solved in Python then reimplemented in C

#include <stdio.h>

//#define INPUTFILE "testdata.txt"
//#define INPUTLEN 10
#define INPUTFILE "../01data.txt"
#define INPUTLEN 2000

int main(void) {
    FILE *fptr;
    if ((fptr = fopen(INPUTFILE, "r")) == NULL) {
       printf("Error opening file\n");
       return 1;
    }
    int depths[INPUTLEN] = {0};
    for (int line = 0; line < INPUTLEN; line++) {
        fscanf(fptr, "%d", &depths[line]);
    }
    fclose(fptr);

    // Part 1
    int counter = 0;
    int comparator = depths[0];
    for (int n = 0; n < INPUTLEN; n++) {
        if (depths[n] > comparator) {
            counter++;
        }
        comparator = depths[n];
    }
    printf("%i\n", counter);

    // Part 2
    counter = 0;
    comparator = depths[0] + depths[1] + depths[2];
    int windowsum = 0;
    for (int n = 0; n < INPUTLEN - 2; n++) {
        windowsum = depths[n] + depths[n + 1] + depths[n + 2];
        if (windowsum > comparator) {
            counter++;
        }
        comparator = windowsum;
    }
    printf("%i\n", counter);

    return 0;
}
