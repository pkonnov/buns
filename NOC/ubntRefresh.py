#!/usr/bin/python3.4

import paramiko
import getpass
import sys
import time

c0 = 'sed -i "s/users.1.name=ubnt/users.1.name=[ ]/" /tmp/system.cfg'
c1 = 'cfgmtd -f /tmp/system.cfg -w'
c2 = '/usr/etc/rc.d/rc.softrestart save'
c3 = 'passwd name'
c4 = [pass]
c5 = [pass]
c6 = 'cfgmtd -f /tmp/system.cfg -w'
c7 = '/usr/etc/rc.d/rc.softrestart save'


USER = [ ]
PASSWORD = [ ] #getpass.getpass()
PASSWORD1 = [ ]
PASSWORD2 = [ ]
# ENABLE_PASS = getpass.getpass(prompt='Enter enable password: ')

DEVICES_IP = [list_ip]

for IP in DEVICES_IP:
    print('Connection to device {}'.format( IP ))
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    try:
        client.connect(hostname=IP, username=USER, password=PASSWORD1,
                       look_for_keys=False, allow_agent=False)
    except paramiko.ssh_exception.AuthenticationException:
        client.connect(hostname=IP, username=USER, password=PASSWORD2,
                       look_for_keys=False, allow_agent=False)
    # except paramiko.ssh_exception.AuthenticationException:
    #     client.connect(hostname=IP, username=USER, password=PASSWORD2,
    #                    look_for_keys=False, allow_agent=False)

    with client.invoke_shell() as ssh:
        ssh.send(c0 + '\n')
        time.sleep(4)
        ssh.send(c1 + '\n')
        time.sleep(4)
        ssh.send(c2 + '\n')
        time.sleep(10)
        ssh.send(c3 + '\n')
        time.sleep(10)
        ssh.send(c4 + '\n')
        time.sleep(4)
        ssh.send(c5 + '\n')
        time.sleep(10)
        ssh.send(c6 + '\n')
        time.sleep(10)
        ssh.send(c7 + '\n')
        time.sleep(10)

        result = ssh.recv(5000).decode('utf-8')
        r = open('finished.txt', 'w')
        r.write(result + '\n')
        r.close()
        print(result)

# sed -i 's/users.1.name=ubnt/users.1.name=[ ]/' /tmp/system.cfg

