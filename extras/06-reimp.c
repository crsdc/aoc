// https://adventofcode.com/2021/day/6
// Solved in Python then reimplemented part 2 method in C

#include <stdio.h>
#include <stdlib.h>

#define INPUTFILE "../06data.txt"
#define INPUTLEN 300
#define DAYS 256

// Iterate over array adding all values to get total fish population
void printtotal (unsigned long int fishcounts[]) {
    unsigned long int fishtotal = 0;
    for (int i = 0; i <= 8; i++) {
        fishtotal += fishcounts[i];
    }
    printf("total %lu\n", fishtotal);
}

int main(void) {

    // Read in input
    int input[INPUTLEN];
    FILE *fptr;
    if ((fptr = fopen(INPUTFILE, "r")) == NULL) {
        printf("Error opening file\n");
        return 1;
    }
    for (int number = 0; number <= INPUTLEN; number++) {
        fscanf(fptr, "%d%*c", &input[number]);
    }
    fclose(fptr);

    // Count from input how many fish have each timer setting
    unsigned long int fishcounts[9] = {0};
    for (int i = 0; i < INPUTLEN; i++) {
        fishcounts[input[i]]++;
    }

    // Note how many fish on 0 and move all fish down a day
    unsigned long int newfish = 0;
    for (int day = 1; day <= DAYS; day++) {
        newfish = fishcounts[0];
        for (int timer = 0; timer < 8; timer++) {
            fishcounts[timer] = fishcounts[timer + 1];
        }
        // Add in populations of new fish and reset fish previously on 0 to 6
        fishcounts[8] = newfish;
        fishcounts[6] += newfish;
        // Part 1 result at day 80
        if (day == 80) {
            printtotal(fishcounts);
        }
    }
    // Part 2 results at day 256
    printtotal(fishcounts);

    return 0;
}
