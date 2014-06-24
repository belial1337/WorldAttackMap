#!/usr/bin/python
events = "/var/www/map/events"
with open(events) as f:
	content = f.read().splitlines()
	f.close()
for line in content:
	print len(line)
	print line
