#!/bin/bash

# FILES OLDER THAN THIS NUMBER OF DAYS WILL BE REMOVED 
DELAY=14

if [ "$(id -u)" == "0" ]; then
	cd /var/log 

	# display the disk usage before cleanup
	# /bin/df -h .
	/usr/bin/du -sh /var/log

	# list all the files before removing
	/usr/bin/find /var/log/* -type f -mtime +${DELAY} -exec ls -la {} \;

	# remove the files
	/usr/bin/find /var/log/* -type f -mtime +${DELAY} -exec rm {} \;

	# display the disk usage after cleanup
	# /bin/df -h .
	/usr/bin/du -sh /var/log
else
	echo "ERROR: Must be root to run script."
fi
#End
