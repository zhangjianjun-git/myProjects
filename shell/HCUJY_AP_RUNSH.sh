#!/bin/sh

#user define shell
VERSION="1"
MODIFIED_TIME="09/02/2013"
DEPLOY_UNION="HCUJY_AP"
EDITER_MAIL="caoguangping.zh"

[ $# -lt 1 ] && { echo "Usage: $0 shellname [shellparm] <quiet>"; exit; }
#2 parm,First is shell name,second is shell parm
sh $@
if [ $? = 0 ] 
then
	echo "Finish"
	exit 0
else
	echo "Error"
	exit 1
fi