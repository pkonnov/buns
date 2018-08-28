#!/usr/bin/python3.6
import socket, threading, time

key = 8194

shutdown = False
join = False

def receving(name, sock):
	while not shutdown:
		try:
			while True:
				data, addr = sock.recvfrom(1024)
				# print(data.decode('utf-8'))

				# begin
				decrypt = ''; k = False
				for i in data.decode('utf-8'):
					if i == ':':
						k = True
						decrypt += i
					elif k == False or i == ' ':
						decrypt += i
					else:
						decrypt += chr(ord(i)^key)
				print(decrypt)
				# end

				time.sleep(0.2)

		except:
			pass