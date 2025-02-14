#!/bin/sh

#standard backup
VERSION="3"
MODIFIED_TIME="20140310"
DEPLOY_UNION="HCUJY_AP"
EDITER_MAIL="ECTIP.zh"

LOG_HOME=/home/ap/$LOGNAME/app_log
[ -d $LOG_HOME ] || { mkdir $LOG_HOME -p; }
LOG_FILE=$LOG_HOME/standard_backup.log   #log file

BackupDir=/home/ap/$LOGNAME/update/$1/backup;
[ -d $BackupDir ] || { mkdir -p $BackupDir; }

cd /home/ap/$LOGNAME
[ -f $BackupDir/domains.tar* ] && { echo "Backup Repeat"; exit 1; }
tar cvPf $BackupDir/domains.tar.$1 --exclude=domains/logs --exclude=domains/USRDOM --exclude=domains/*/logs --exclude=domains/*/tmp /home/ap/lnsjcj/domains 1>>$LOG_FILE;
tar uvf $BackupDir/domains.tar.$1 domains/USRDOM/config/config.xml domains/USRDOM/config/jdbc 1>>$LOG_FILE;
[ -d /home/ap/$LOGNAME/domains/USRDOM/servers/AdminServer/upload ] && { tar uvf $BackupDir/domains.tar.$1 domains/USRDOM/servers/AdminServer/upload 1>>$LOG_FILE; }

echo "BackUp OK"
exit 0