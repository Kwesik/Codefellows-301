# Script:   PythonHw
#Author:    Kwesik
#Last rev: 20210907
#Purpose:   Python variables in bash

#Run in sudo bash

echo  BEFORE CONTENTS 
cat /var/log/syslog
cat /var/log/wtmp

echo -n "" > /var/log/syslog
echo -n "" > /var/log/wtmp

echo  AFTER CONTENTS 
cat /var/log/syslog
cat /var/log/wtmp

#End
