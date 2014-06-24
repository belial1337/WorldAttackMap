#!/usr/bin/python
import socket
import re
import binascii
import struct
import time
import sys
from random import randint
from base64 import b64encode
from hashlib import sha1
from thread import *

events = "/var/www/map/eventstream"

with open(events) as f:
	content = f.read().splitlines()
	f.close()




websocket_answer = (
   'HTTP/1.1 101 Switching Protocols',
   'Upgrade: websocket',
   'Connection: Upgrade',
   'Sec-WebSocket-Accept: {key}\r\n\r\n',
)
 
GUID = "258EAFA5-E914-47DA-95CA-C5AB0DC85B11"
 
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print 'Socket Created'
try:
	s.bind(('192.168.1.101', 443))
except socket.error as msg:
	print 'Bind failed. Error Code : ' + str(msg[0]) + ' Message ' + msg[1]
	sys.exit()
print 'Socket bind complete'
s.listen(10)
print "Listening for connections"

def clientthread(client):
	while True:	
		for line in content:
			print 'Function 1'
			length = len(line)
                       	preamble = "\x81\x7e" + struct.pack(">i", length)[2:]
                        client.send(preamble+line)
                        print "Sending Attack Event Size: " + hex(length) + " Bytes\n"
                        time.sleep(randint(0,3))
		client.close()


while 1:
	client, address = s.accept()
	print 'Got connection from', address
	text = client.recv(1024)
	print text
  	key = (re.search('Sec-WebSocket-Key:\s+(.*?)[\n\r]+', text)
        .groups()[0]
        .strip())

        response_key = b64encode(sha1(key + GUID).digest())
        response = '\r\n'.join(websocket_answer).format(key=response_key)
		
	print response
	client.send(response)
	client.recv(1)
	start_new_thread(clientthread ,(client,))
s.close()
