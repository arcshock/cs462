CC = gcc
CXX = g++

C_FLAGS = --std=c11
CXX_FLAGS = -std=c++11 -pipe
ARCHFLAGS = -m32
CFLAGS_DEBUG = -Wall -g 


all:
	$(CC) $(C_FLAGS) $(CFLAGS_DEBUG) $(ARCHFLAGS) cs462_bjfrost2_A09_part1.c -o part1.elf
	$(CXX) $(ARCHFLAGS) $(CXX_FLAGS) $(CFLAGS_DEBUG) cs462_bjfrost2_A09_part3.cpp -o part3.elf
