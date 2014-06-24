#!/usr/bin/python
import struct
stringtest0 = ('this is a string test dude')
stringtest = ('{"latitude":"45.48","longitude":"-73.50","countrycode":"CA","country":"CA","city":"Saint-lambert","org":"Nu Networx","latitude2":"45.48","longitude2":"-73.50","countrycode2":"CA","country2":"CA","city2":"Saint-lambert","type":"ipviking.honey","md5":"174.142.126.48","dport":"17500","svc":"17500","zerg":""}')
stringlen = len(stringtest)
preamble = '\x41\x41' 
#print stringlen
print preamble + struct.pack(">i", stringlen)[2:] 
#print struct.pack(">i", 26)
