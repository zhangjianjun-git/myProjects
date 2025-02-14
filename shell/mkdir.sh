#!/bin/sh
[ -d  /home/ap/$LOGNAME/domains/lib ] || { mkdir /home/ap/$LOGNAME/domains/lib -p; }
[ -d  /home/ap/$LOGNAME/domains/eplib ] || { mkdir /home/ap/$LOGNAME/domains/eplib -p; }
[ -d  /home/ap/$LOGNAME/domains/dist/dclasses/com ] || { mkdir /home/ap/$LOGNAME/domains/dist/dclasses/com -p; }

cd /home/ap/$LOGNAME/domains/USRDOM

server1=$(ls start_*.sh|grep -v "_1"|grep -v "AdminServer"|awk -F"." '{print $1}'|awk -F"start_" '{print $2}')

[ -d  /home/ap/$LOGNAME/domains/logs/$server1/logs/tranlog ] || { mkdir /home/ap/$LOGNAME/domains/logs/$server1/logs/tranlog -p; }
exit 0
