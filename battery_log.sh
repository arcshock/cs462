#!/bin/bash
#Author: Brahm Lower, Bucky Frost
#Purpose: Output Android battery log data to stdout

readonly LOG_PATH="./"
readonly LOG_FILE="BatteryLog.csv"
main(){
	cat $LOG_PATH$LOG_FILE 
}

main
