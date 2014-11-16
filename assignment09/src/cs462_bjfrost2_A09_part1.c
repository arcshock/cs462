/**
 * Bucky Frost
 * CS 462
 * File: cs462_bjfrost2_A09_part1.c
 * Purpose: A multifuntion program that will be investigated with the use of ida.
 */

#include <stdio.h>
#include <stdlib.h>
#include <string.h>

char* strflip(char *str);

int main(int argc, char **argv)
{
	if (argc == 2) {
		char *flipped_arg = strflip(argv[1]);
		  printf("%s\n",flipped_arg);
		free (flipped_arg);
	}
	exit(0);
}

/**
 * function strflip
 *
 * Takes a pointer to a c string.
 *
 * Returns a pointer to memory allocated for a string that is inverted 
 * input string.
 */
char* strflip(char *str)
{
	int string_size = strlen(str);

	char *flipped_string = (char *)malloc(sizeof(char)*string_size);

	int flip_counter = string_size - 1;

	for (int ii = 0; ii < string_size; ++ii) {
		flipped_string[ii] = str[flip_counter--];
	}

	return flipped_string;
}
