# pingToCsv

Pings one or several addresses and outputs the result in a csv file

For windows you have to change -c to -n when calling ping

scv format:
success, address, icmp_seq, tll, time
or if timeStamp is True
timestamp, success, address, icmp_seq, tll, time
