#!/bin/bash

#war包所在路径
WAR_PATH=""
#待更新文件所在目录
CLS_DIR=""
#待更新文件路径描述文件
CLS_PATH_DESC=""
#name of the war
WAR_NAME=""

JAR_SCOPE="";

#start parse args
NO_ARGS=0
E_OPTERROR=65

if [ $# -eq "$NO_ARGS" ]        #script invoked with no command-line args?
then
  echo "Usage:`basename $0` options (-mnopqrs)"
  exit $E_OPTERROR        #Exit and explain usage.
                          #Usage:scriptname -options
                          #Note:dash (-) necessary
fi

while getopts "w:c:p:h" Option
do
 case $Option in
    w)
      #war包所在目录
      WAR_PATH=$OPTARG;;
    c)
      CLS_DIR=$OPTARG;;
    p)
      CLS_PATH_DESC=$OPTARG;;
    h)
      echo "-w --war Path,必选项,war包所在路径"
      echo "-c --classes directory,必选项,classes所在目录 "
      echo "-p --class path describle file path,可选项,需要"
      echo "     更新的文件的路径描述文件,一般.class文件会自动"
      echo "     反编译得到其全限定名，而其他文件为避免出错最好"
      echo "     手工指定路径"
      echo "-h 帮助"
      exit 0;;
    ?)
      echo "unkown parameters"
      exit 1;;
 esac
done
#end parse args


if [ -z "$WAR_PATH" ]; then
  echo "需要指定war包所在路径"
  echo "运行autoUpdataWar.sh -h查看使用说明"
  exit 1
fi

if [ -z "$CLS_DIR" ]; then
  echo "需要指定增量文件所在的目录"
  echo "运行autoUpdataWar.sh -h查看使用说明"
  exit 1
fi

#tart unzip target war
function hwar(){
	workdir=$1

	classdir="$workdir/tmp"
	mkdir $classdir

	targetWar=${2##*/}

        if [[ $targetWar =~ ^(scms-.+\.war) ]]; then
             JAR_SCOPE="scms-*\.jar" 
        elif [[ $targetWar =~ ^(nps-platform.+\.war) ]]; then
             JAR_SCOPE="nps-platform-*\.jar" 
        else
             echo "非scms/nps的war包需要手工指定jar包范围"
             exit 0
        fi
       
        WAR_NAME=${targetWar%.*}
	wardir="$classdir/${targetWar%.*}"
	mkdir $wardir

#对每个找到的 JAR 文件：
 #提取文件名（去掉路径）。
 #构造一个目标目录路径（去掉文件扩展名）。
 #创建目标目录。
 #解压 JAR 文件到目标目录
	unzip -oq $2 -d ${wardir}
	#echo $wardir
	for jars in `find $wardir -name "$JAR_SCOPE"`
	do
		jarName=${jars##*/}
		jardir="$classdir/${jarName%.*}"
		mkdir $jardir
		#echo "${jars}:${jardir}"
		unzip -oq $jars -d $jardir
	done
}
echo "start unzip target war..."
workDir="/root/bin"
hwar $workDir $WAR_PATH
#end handle old war


#start parse classes package info
echo "get package info of files to be updated..."
cd $CLS_DIR
#echo "$cd $CLS_DIR"
for file in `ls ./`
do
${JAVA_HOME}/bin/javap ${file%.*} | grep ' class ' |awk -F ' ' '{if($3=="class"){print $4}else{print $3}}' >> ./pkInfo.txt
done
#end process classes

#start update class
echo "start update..."
workWarDir="${workDir}/tmp"
if [ ! -x "$workWarDir" ];then
  echo "error 11"
  exit 1
fi

for cls in `cat ${CLS_DIR}/pkInfo.txt`
do
  clsname=${cls##*.}
  for odcls in `find ${workWarDir} -name "${clsname}*\.class"`
     do
       for newCls in `ls ${CLS_DIR} |grep ${clsname}`
          do
           cp -f ${CLS_DIR}/${newCls} ${odcls}
         done
     done
done

#start rewar the package
echo "start rejar the package..."
jardirinwar="WEB-INF/lib"
cd $workdir/tmp
for jarfolder in `ls ./`
do
  if [ -d $jarfolder -a  "$WAR_NAME" != "$jarfolder" ];then
     #echo "$jarfolder"
     $JAVA_HOME/bin/jar cf ${jarfolder}.jar -C $jarfolder/ .
     mv ./${jarfolder}.jar ./${WAR_NAME}/${jardirinwar}
  fi
done
echo "start rewar the package..."
$JAVA_HOME/bin/jar cf ${WAR_NAME}.war -C ${WAR_NAME}/ .
mv ${WAR_NAME}.war ${WAR_PATH%/*}/${WAR_NAME}.warnew

rm -rf $workdir/tmp
