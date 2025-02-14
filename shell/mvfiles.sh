#!/bin/sh
FileHandle()
{
        Count=`ls $1 2>/dev/null |wc -l`;
        if [ $Count -gt 0 ]
        then
                cp $1 $2
        fi
}

if [ "$1" = "" ] 
then
        echo "mvfiles.sh yyyymmdd"
        exit 1
fi
cd /home/ap/$LOGNAME/update/$1
if [ -f hcums_eframework_lib_v*.jar ]
then
	rm -rf /home/ap/$LOGNAME/domains/lib/hcums_eframework_lib_v*.jar
	cp hcums_eframework_lib_v*.jar /home/ap/$LOGNAME/domains/lib
fi


if [ -f hcums_eframework_v1*.jar ]
then 
    jarname=`ls hcums_eframework_v1*.jar|head -1`
	mkdir hcums_eframework_temp
	cd hcums_eframework_temp
	
	cp /home/ap/$LOGNAME/domains/eplib/hcums_eframework_v1*.jar .
	jar -xvf hcums_eframework_v1*.jar > /dev/null 
	rm -rf hcums_eframework_v1*.jar
	
	cp /home/ap/$LOGNAME/update/$1/hcums_eframework_v1*.jar .
	jar -xvf hcums_eframework_v1*.jar > /dev/null 
	rm -rf hcums_eframework_v1*.jar
	
	jar cvf "$jarname" *
	rm -rf /home/ap/$LOGNAME/domains/eplib/hcums_eframework_v1*.jar
	cp hcums_eframework_v1*.jar /home/ap/$LOGNAME/domains/eplib
	
	cd /home/ap/$LOGNAME/update/$1
fi
if [ -f P1_v*.jar ]
then
	#rm -rf /home/ap/$LOGNAME/domains/eplib/P1_v*.jar
	#cp P1_v*.jar /home/ap/$LOGNAME/domains/eplib
	
	
	jarname=`ls P1_v*.jar|head -1`
	mkdir P1_temp
	cd P1_temp
	
	cp /home/ap/$LOGNAME/domains/eplib/P1_v*.jar .
	jar -xvf P1_v*.jar > /dev/null 
	rm -rf P1_v*.jar
	
	cp /home/ap/$LOGNAME/update/$1/P1_v*.jar .
	jar -xvf P1_v*.jar > /dev/null 
	rm -rf P1_v*.jar
	
	jar cvf "$jarname" *
	rm -rf /home/ap/$LOGNAME/domains/eplib/P1_v*.jar
	cp P1_v*.jar /home/ap/$LOGNAME/domains/eplib
	
	cd /home/ap/$LOGNAME/update/$1
fi

if [ -f hcums_1*.jar ] 
then
	#rm -rf /home/ap/$LOGNAME/domains/eplib/hcums_1*.jar
	#cp hcums_1*.jar /home/ap/$LOGNAME/domains/eplib
	
	jarname=`ls hcums_1*.jar|head -1`
	mkdir hcums_temp
	cd hcums_temp
	
	cp /home/ap/$LOGNAME/domains/eplib/hcums_1*.jar .
	jar -xvf hcums_1*.jar > /dev/null 
	rm -rf hcums_1*.jar
	
	cp /home/ap/$LOGNAME/update/$1/hcums_1*.jar .
	jar -xvf hcums_1*.jar > /dev/null 
	rm -rf hcums_1*.jar
	
	jar cvf "$jarname" *
	rm -rf /home/ap/$LOGNAME/domains/eplib/hcums_1*.jar
	cp hcums_1*.jar /home/ap/$LOGNAME/domains/eplib
	
	cd /home/ap/$LOGNAME/update/$1
fi
if [ -f  hcums_dist_1*.jar ]
then
	rm -rf  /home/ap/$LOGNAME/domains/dist/hcums_dist_1*.jar
	cp hcums_dist_1*.jar /home/ap/$LOGNAME/domains/dist
fi
if [ -f hcums_service_1*.jar ]
then
	rm -rf /home/ap/$LOGNAME/domains/dist/dclasses/hcums_service_1*.jar
	cp hcums_service_1*.jar /home/ap/$LOGNAME/domains/dist/dclasses
fi

if [ -d /home/ap/$LOGNAME/domains/USRDOM/servers/AdminServer/upload ]
then
	FileHandle '*.ear' /home/ap/$LOGNAME/domains/USRDOM/servers/AdminServer/upload
	FileHandle '*.war' /home/ap/$LOGNAME/domains/USRDOM/servers/AdminServer/upload
fi
exit 0
