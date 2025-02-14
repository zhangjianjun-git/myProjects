#/bin/sh
LOG_DIR=/home/ap/$LOGNAME/app_log      #log file
[ -d $LOG_DIR ] || { mkdir $LOG_DIR; }
LOG_FILE=$LOG_DIR/deploy.log
cd /home/ap/$LOGNAME/domains/lib
if [ -f hcums_eframework_lib_v*.jar ]
then
	jar -xvf hcums_eframework_lib_v*.jar > $LOG_FILE
	rm -rf hcums_eframework_lib_v*.jar
	rm -rf META-INF
fi
cd /home/ap/$LOGNAME/domains/dist
if [ -f hcums_dist_1*.jar ]
then
	jar -xvf hcums_dist_1*.jar >> $LOG_FILE
	rm -rf hcums_dist_1*.jar
	rm -rf META-INF
fi
cd /home/ap/$LOGNAME/domains/dist/dclasses
if [ -f hcums_service_1*.jar ]
then
	find . -name *.class -exec rm -rf {} \;
	jar -xvf hcums_service_1*.jar >> $LOG_FILE
	rm -rf hcums_service_1*.jar
	rm -rf META-INF
fi

cd /home/ap/$LOGNAME/domains/USRDOM



server1=$(ls start_*.sh|grep -v "_1"|grep -v "AdminServer"|awk -F"." '{print $1}'|awk -F"start_" '{print $2}')



cd /home/ap/$LOGNAME/domains/dist/epconf
if [ -f system_AppServer1.properties ]
then
	cp system_AppServer1.properties system_$server1.properties
	cat system_$server1.properties|sed "s/AppServer1/$server1/g">tmpa
	mv tmpa system_$server1.properties
fi


if [ -f log4j_AppServer1.xml ]
then
	cp log4j_AppServer1.xml log4j_$server1.xml
	cat log4j_$server1.xml|sed "s/AppServer1/$server1/g">tmpa
	mv tmpa log4j_$server1.xml
fi

if [ -f /home/ap/$LOGNAME/domains/dist/USRDOM/system_$server1.properties ] 
then
	rm -rf /home/ap/$LOGNAME/domains/dist/USRDOM/system_$server1.properties
fi



if [ -f /home/ap/$LOGNAME/domains/dist/USRDOM/log4j_$server1.properties ]
then
        rm -rf /home/ap/$LOGNAME/domains/dist/USRDOM/log4j_$server1.properties
fi


exit 0
