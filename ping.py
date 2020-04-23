import subprocess
import csv
import os
import time


#setup
addresses = ["8.8.8.8", "192.168.0.5"]
tries = 10
timeStamp = False
fileName = "pings.csv"
writeMode = 'w'
newlinechar = ''
#-------------------------


output = []

for address in addresses:
    success = True
    try:
        res = subprocess.check_output(['ping', '-c', str(tries), address])
    except:
       success = False
    #print(res)
    if success:
        res = res.splitlines()[1:1+tries]
        for i in range(0, tries):
            res[i] = "success "+res[i].decode('utf-8')
        output.append(res)
    else:

        output.append(["fail "+address])

fileExists = os.path.exists(fileName)   
with open(fileName, writeMode, newline=newlinechar) as file:
    writer = csv.writer(file)
    if ((not fileExists) and writeMode == 'a') or writeMode == 'w':
        if timeStamp:
            writer.writerow(["timeStamp", "success", "address", "icmp_seq", "ttl", "time"])
        else:
            writer.writerow(["success", "address", "icmp_seq", "ttl", "time"])
         
    for address in output:
        for l in address:
            l = l.split(' ')
            if(l[0] == "success"):
                l[4] = l[4].replace(":","")
                l[5] = l[5].replace("icmp_seq=","")
                l[6] = l[6].replace("ttl=","")
                l[7] = l[7].replace("time=","")
                if timeStamp:
                    writer.writerow([time.time(), l[0], l[4], l[5], l[6], l[7]])
                else:
                    writer.writerow([l[0], l[4], l[5], l[6], l[7]])
            else:
                if timeStamp:
                    writer.writerow([time.time(), l[0], l[1], None, None, None])
                else:
                    writer.writerow([l[0], l[1], None, None, None])
        
        
