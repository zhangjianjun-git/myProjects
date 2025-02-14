#!/bin/sh

[ $# -lt 1 ] && { echo "Usage: $0 yyyymmdd01 <quiet>"; exit; }
#new dir ---manu

#backup ---sh
sh /home/ap/lnsjcj/bin/HCUJY_AP_CUSTOM_BACKUP.sh $1
#dist  --manu

#stop  --sh

sh /home/ap/lnsjcj/bin/HCUJY_AP_SERVICE.sh stop
#patch --sh
sh /home/ap/lnsjcj/bin/HCUJY_AP_RUNSH.sh onkeydpl.sh $1
#start --sh
sh /home/ap/lnsjcj/bin/HCUJY_AP_SERVICE.sh start
