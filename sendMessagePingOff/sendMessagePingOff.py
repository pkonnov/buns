#!/usr/bin/python3

'''
получаем каждые 2 мин response
если не пингуется то шлем сообщение на почту
'''
import requests
#from urllib3.exceptions import HTTPError as BaseHTTPError

def getResponse():

	r = requests.get('')
	rS = str(r.status_code)
	if rS == '403':
		print('403')
	else:
		print('ahooeno')


if __name__ == '__main__':
	getResponse()