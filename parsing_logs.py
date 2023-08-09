import re
from collections import Counter
import csv

logfile="prod_404_api.neovee_log.log" #please put your own log file name 
logreg="\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}"
with open(logfile) as f:
    log = f.read()
    ip_list = re.findall(logreg, log)
#    for k,v in Counter(ip_list).items():
#        print(k,":",v)
    with open("ipcount.csv", "w") as f:
        fwritercsv = csv.writer(f)
        fwritercsv.writerow(["IP_ADRESS", "COUNT"])
        for k,v in Counter(ip_list).items():
            fwritercsv.writerow([k,v])

