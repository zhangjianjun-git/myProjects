#!/bin/sh

VERSION="13"
MODIFIED_TIME="20140320"
DEPLOY_UNION="HCUJY_AP"
EDITER_MAIL="ECTIP.zh@ccb.com"
    
LOG_HOME=$HOME/log/start_stop
[ -d $LOG_HOME ] || { mkdir -p $LOG_HOME; }
Usage()
{
        echo " Please Usage: `basename $0` [start|stop|restart] "
        exit 1
}

##*****************************************************************************************************************************************************************##
#######################################################################main shell###################################################################################
##*****************************************************************************************************************************************************************##


###############################################################other echo usage notice############################################################################
if [[ "$1" != "stop" && "$1" != "start" && "$1" != "restart" ]] 
then
        Usage
fi


######################################################################stop all######################################################################################
 
if [[ "$1" == "stop" ]]
 then
# Call setDomainEnv here because we want to have shifted out the environment vars above
    DOMAIN_HOME="/home/ap/$LOGNAME/domains/USRDOM"

	cd $DOMAIN_HOME
	server1=$(ls start_*.sh|grep -v "_1"|grep -v "AdminServer"|awk -F"." '{print $1}'|awk -F"start_" '{print $2}')

	echo "Please wait seconds.........."
    echo "$server1 will stop..........."
	PID=`ps -ef | grep java   | grep   $server1  |  grep   $USER" "  | grep -v grep | awk '{print $2}'`
	if [ ! -z "$PID" ]
	then
		sh $DOMAIN_HOME/stop_$server1.sh 1>$LOG_HOME\stop.$server1.log &
	fi


	wait

	PID=`ps -ef | grep java   | grep   $server1  |  grep   $USER" "  | grep -v grep | awk '{print $2}'`
	if [ ! -z "$PID" ]
	then
		echo "STOP COMMAND FAIL"
		exit 1;
	fi
	echo "$server1 stoped success"



#############################################################shutdown AdminServer####################################################################
#	if [ -f $DOMAIN_HOME/stop_AdminServer.sh ]
#	then
#		echo "Please wait secondes.........."
#	    echo "AdminServer will stop..........."
#		sh $DOMAIN_HOME/stop_AdminServer.sh 1>$LOG_HOME\stop.AdminServer
#	fi
###########################################################shutdown AdminServer over#################################################################
       
 	echo "STOP COMMAND SUCCESS"      
 	exit 0   
fi
 

#######################################################################start all###########################################################################


if [[ "$1" == "start" ]]
 then
# Call setDomainEnv here because we want to have shifted out the environment vars above
	DOMAIN_HOME="/home/ap/$LOGNAME/domains/USRDOM"
# Read the environment variable from the console.
  

	cd $DOMAIN_HOME
	
	server1=$(ls start_*.sh|grep -v "_1"|grep -v "AdminServer"|awk -F"." '{print $1}'|awk -F"start_" '{print $2}')

	##################################################################startup AdminServer over###################################################################
	if [ -f $DOMAIN_HOME/start_AdminServer.sh ]
	then
		PID=`ps -ef | grep java  | grep   AdminServer  |  grep   $USER" "  | grep -v grep | awk '{print $2}'`
		if [ ! -z "$PID" ]; then
			break;
		fi
		  echo "Please wait secondes.........."
	    echo "AdminServer will start..........."
	    while [ true ]
		do
		PID=`ps -ef | grep java  | grep   AdminServer  |  grep   $USER" "  | grep -v grep | awk '{print $2}'`
		if [ ! -z "$PID" ]; then
			echo "AdminServer running..........."
			break;
		fi
		sh $DOMAIN_HOME/start_AdminServer.sh 1>$LOG_HOME\start.AdminServer.log &
		sleep 5
		done
	fi

	
	echo "Please wait secondes.........."
    echo "$server1 will start..........."
    while [ true ]
	do
	PID=`ps -ef | grep java  | grep   $server1  |  grep   $USER" "  | grep -v grep | awk '{print $2}'`
	if [ ! -z "$PID" ]; then
		echo "$server1 running..........."
		break;
	fi
	sh $DOMAIN_HOME/start_$server1.sh 1>$LOG_HOME\start.$server1.log &
	sleep 5
	done

	


    echo "START COMMAND SUCCESS"  
    exit 0
fi



#############################################################restart ALL###################################################################################################################################################################

if [[ "$1" == "restart" ]]
 then
# Call setDomainEnv here because we want to have shifted out the environment vars above
    DOMAIN_HOME="/home/ap/$LOGNAME/domains/USRDOM"
# Read the environment variable from the console.
	cd $DOMAIN_HOME
	server1=$(ls start_*.sh|grep -v "_1"|grep -v "AdminServer"|awk -F"." '{print $1}'|awk -F"start_" '{print $2}')

	echo "Please wait seconds.........."
    echo "$server1 will stop..........."
	PID=`ps -ef | grep java |  grep   $server1  |  grep   $USER" "  | grep -v grep | awk '{print $2}'`
	if [ ! -z "$PID" ]
	then
		sh $DOMAIN_HOME/stop_$server1.sh 1>$LOG_HOME\stop.$server1.log &
	fi

	
	wait

	PID=`ps -ef | grep java   | grep   $server1  |  grep   $USER" "  | grep -v grep | awk '{print $2}'`
	if [ ! -z "$PID" ]
	then
		echo "STOP COMMAND FAIL"
		exit 1;
	fi
	echo "$server1 stoped success"

	

	if [ -f $DOMAIN_HOME/start_AdminServer.sh ]
	then
		PID=`ps -ef | grep java  | grep   AdminServer  |  grep   $USER" "  | grep -v grep | awk '{print $2}'`
		if [ ! -z "$PID" ]; then
			break;
		fi
		echo "Please wait secondes.........."
	    echo "AdminServer will start..........."
	    while [ true ]
		do
		PID=`ps -ef | grep java  | grep   AdminServer  |  grep   $USER" "  | grep -v grep | awk '{print $2}'`
		if [ ! -z "$PID" ]; then
			echo "AdminServer running..........."
			break;
		fi
		sh $DOMAIN_HOME/start_AdminServer.sh 1>$LOG_HOME\start.AdminServer.log &
		sleep 5
		done
	fi

	echo "Please wait secondes.........."
    echo "$server1 will start..........."
    while [ true ]
	do
	PID=`ps -ef | grep java   | grep   $server1  |  grep   $USER" "  | grep -v grep | awk '{print $2}'`
	if [ ! -z "$PID" ]; then
		echo "$server1 running..........."
		break;
	fi
	sh $DOMAIN_HOME/start_$server1.sh 1>$LOG_HOME\start.$server1.log &
	sleep 5
	done



	echo "RESTART COMMAND SUCCESS"
	exit 0
fi