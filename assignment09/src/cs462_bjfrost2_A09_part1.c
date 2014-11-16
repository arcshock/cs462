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
char* strdoubler(char *str);

int main(int argc, char **argv)
{
	if (argc == 2) {
		char *flipped_arg = strflip(argv[1]);
		  printf("%s\n",flipped_arg);
		free (flipped_arg);
	}

	if (argc == 2) {
		char *doubled_arg = strdoubler(argv[1]);
		printf("%s\n",doubled_arg);
		free (doubled_arg);
	}
	exit(0);
}

/**
 * function strdoubler
 *
 * Takes a pointer to a c string.
 *
 * Returnas a pointer to memory allocated for a string that has repeated
 * the characters of a string.
 *
 * Example: abc => aabbcc
 */
char* strdoubler(char *str)
{
	int string_size = strlen(str);

	char *doubled_string = (char *)malloc(sizeof(char)*string_size);

	int doubler_size = string_size*2 - 1;
	int str_index = 0;

	for (int ii = 0; ii < doubler_size; ++ii) {
		doubled_string[ii++] = str[str_index];
		doubled_string[ii] = str[str_index++];
	}

	return doubled_string;
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
