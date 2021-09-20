#Script:        Clear Log
#Author:         Kwesik
#Date:           9/19/2021
#Purpose:       Clear syslog

# Clear syslog and wtmp files with a script.
#SYS variable defines the path for syslog, for the sake of ease. WTMP variable defines the path for wtmp, for the sake of ease.
#Main

SYS=/var/log/syslog
WTMP=/var/log/wtmp

cat $SYS
cat $WTMP
truncate -s 0 $SYS
truncate -s 0 $WTMP
cat $SYS
cat $WTMP

#End