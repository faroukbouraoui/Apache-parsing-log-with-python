import re
from collections import Counter
logfile="****" #please put your own log file name 
logreg="\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}"
with open(logfile) as f:
    log = f.read()
    ip_list = re.findall(logreg, log)
    for k,v in Counter(ip_list).items():
        print(k,":",v)
    