#!/usr/bin/python3.6
import socket, time

host = socket.gethostbyname(socket.gethostname()) # 192.168.0.1
port = 9090 # not admins pasport

clients = []

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) #tcp ip
s.bind((host,port)) # up server

quit = False
print('[server startet]')

while not quit:
	try:
		data, addr = s.recvfrom(1024)

		if addr not in clients:
			clients.append(addr)

		itsatime = time.strftime('%Y-%m-%d-%H.%M.%S', time.localtime())

		print('[' + addr[0] + ']=[' + str(addr[1]) + ']=[' + itsatime + ']/', end='')
		print(data.decode('utf-8'))

		for client in clients:
			if addr != client:
				s.sendto(data, client)

	except:
		print('\n[ server stoped ]')
		qiut = True

s.close()