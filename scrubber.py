#!/usr/bin/env python

import os, sys

readFile = open("eventstream3")

lines = readFile.read().splitlines()

readFile.close()
w = open("eventstream4",'w')

for line in lines:
	w.writelines(line[5:]+"\n")

w.close()
