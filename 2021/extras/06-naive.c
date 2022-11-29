// https://adventofcode.com/2021/day/6
// Naive method to solve part 1 extended to part 2, where it becomes infeasible

#include <stdio.h>
#include <stdlib.h>

#define INPUTFILE "../06data.txt"
#define INPUTLEN 300
#define DAYS 256

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
    unsigned long int fishcount = sizeof(input) / sizeof(input[0]);

    // Allocate an array that will be extended later as needed
    int *fish = malloc(fishcount * sizeof(int));
    if (fish == NULL) {
        printf("Unable to allocate memory\n");
        return 1;
    }
    for (int i = 0; i < fishcount; i++) {
        fish[i] = input[i];
    }

    // Iteratate over array, reduce timers, determine how many new fish
    int newfish = 0;
    for (int day = 1; day <= DAYS; day++) {
        newfish = 0;
        for (int i = 0; i < fishcount; i++) {
            if (fish[i] > 0) {
                fish[i]--;
            } else {
                newfish++;
                fish[i] = 6;
            }
        }

        // Extend array to accomodate new fish
        int *fish_temp = realloc(fish, (fishcount + newfish) * sizeof(fish[0]));
        if (fish_temp == NULL) {
            printf("Unable to reallocate memory\n");
            free(fish);
            return 1;
        } else {
            fish = fish_temp;
        }

        // Add new fish to array
        for (int i = fishcount; i < fishcount + newfish; i++) {
            fish[i] = 8;
        }
        fishcount = fishcount + newfish;
        printf("%lu bytes for %lu fish at end of day %i\n", fishcount * sizeof(fish[0]), fishcount, day);
    }

    free(fish);
    return 0;
}
