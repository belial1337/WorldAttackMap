#!/usr/bin/python
import struct
string = ('this is a test string duh! wacha talking about willis?')
length = len(string)
#print hex(length)[2:].decode('hex')
test0 = ('1234567910')
test1 = ('{"latitude":"28.18","longitude":"113.11","countrycode":"CN","country":"CN","city":$')
test2 = ('{"latitude":"45.48","longitude":"-73.50","countrycode":"CA","country":"CA","city":')
length = len(test1)
print length
preamble = "\x41\x41\x41" + hex(length)[2:].decode('hex')
print preamble

