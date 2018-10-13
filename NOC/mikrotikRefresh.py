#!/usr/bin/python3.4
import telnetlib
import time
import getpass
import sys

c1 = '/radius add service=login address=[ ] secret=[ ] disabled=no'.encode('utf-8')  #sys.argv[1].encode('utf-8')
c2 = '/user aaa set use-radius=yes'.encode('utf-8')
c3 = '/ip service'.encode('utf-8')
c4 = 'set telnet disabled=yes'.encode('utf-8')
c5 = 'set ftp disabled=yes'.encode('utf-8')
c6 = 'set api-ssl disabled=yes'.encode('utf-8')
c7 = 'set ssh disabled=yes'.encode('utf-8')
c8 = 'set www disabled=yes'.encode('utf-8')
c9 = '/user group'.encode('utf-8')
c10 = 'add name=[ ] policy="local,telnet,ssh,ftp,reboot,read,write,test,winbox,password,web,sniff,sensitive,api,romon,tikapp,!policy,!dude"'.encode('utf-8')
c11 = '/user add name=[ ] password=[ ] group=full'.encode('utf-8')
c12 = '/user remove admin'.encode('utf-8')

USER = '[ ]'.encode('utf-8')
PASSWORD = '[ ]'.encode('utf-8')
ENABLE_PASS = '[ ]'.encode('utf-8')

DEVICES_IP = [list_ip]

for IP in DEVICES_IP:
    print('Connection to device {}'.format(IP))

    t = telnetlib.Telnet(IP)
    t.read_until(b'Login: ')
    t.write(USER + b'\n')

    t.read_until(b'Password:')
    t.write(PASSWORD + b'\n')

    t.read_until(b'>')
    t.write(c1 + b'\r\n')
    t.write(c2 + b'\r\n')
    t.write(c3 + b'\r\n')
    t.write(c4 + b'\r\n')
    t.write(c5 + b'\r\n')
    t.write(c6 + b'\r\n')
    t.write(c7 + b'\r\n')
    t.write(c8 + b'\r\n')
    t.write(c8 + b'\r\n')
    t.write(c9 + b'\r\n')
    t.write(c10 + b'\r\n')
    t.write(c11 + b'\r\n')
    t.write(c12 + b'\r\n')

    time.sleep(4)
