#!/bin/bash

#Author                     Kwesik
#Date of last revision      20210903
#Description of purpose     Clean both syslog and wtmp


#variable
LOG_DIR=/var/log

#main
cd $LOG_DIR
cat /dev/null > syslog
cat /dev/null > wtmp

#function
echo "Logs cleaned up"


#end
exit
