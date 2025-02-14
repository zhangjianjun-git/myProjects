#!/bin/sh
cd $HOME/bin
sh mkdir.sh
if [ $? = 1 ] 
then
	echo "Error"
	exit 1
fi
sh mvfiles.sh $1
if [ $? = 1 ] 
then
	echo "Error"
	exit 1
fi
sh jarxvf.sh
if [ $? = 0 ] 
then
	echo "Finish"
	echo $1>$HOME/domains/dist/epconf/version
	echo `date +%Y-%m-%d' '%T` $1>>$HOME/update/update.log
	exit 0
else
	echo "Error"
	exit 1
fi

