#!/bin/bash
#Script Name:       TimeStamp
#Author:            Kwesik
#Last Rev:          20210831
#Purpose:           copies files to curent directory


date=$(date +"%T")


echo "Copying Syslog to Documents $date"

cp -r /var/log/syslog /home/kwesik/Documents

echo "Switching to documents folder $date"

cd /home/kwesik/Documents/

echo "appending date and time to filename $date"
mv syslog syslog"$(date + "%Y%m%d_%T")"

echo "copy complete $date"

#End