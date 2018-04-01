import requests, fake_useragent
from bs4 import BeautifulSoup
from time import sleep
from termcolor import colored, cprint


l = '--------------------------------------------------------'


#random user
ua = fake_useragent.UserAgent()
user = ua.random
header = {'User-Agent':str(user)}

# my ip
ip_site = 'http://icanhazip.com'
adress  = requests.get(ip_site, headers=header)

print(l + '\n[*] IP your network:\n' + adress.text + l)
print('[!] Connecting tot the Tor network /', end='')

for i in range(5):
	sleep(0.2)
	print('.', end='', flush=True)

proxie ={
	'http': 'socks5h://127.0.0.1:9050',
	'https': 'socks5h://127.0.0.1:9050'
}

try:
	adress = requests.get(ip_site, proxies=proxie, headers=header)
except:
	connection = False
	print(colored('/\n[x] Stopping connect to the Tor network\n', 'red') + l)

# connected
else:
	connection = True
	print('/\n[+] Connected to the Tor network\n' + l)
	print('[*] IP Tor network:\n' + adress.text + l)

# parse_site

finally:
	url = input('\n[!] Uniform Resourse Locator:\nhttp://')

	if connection == True:
		page = requests.get('http://' + str(url.split()[0]), proxies=proxie, headers=header)
	else:
		page = requests.get('http://' + str(url.split()[0]), headers=header) 

	soup = BeautifulSoup(page.text, 'html.parser')

	if url.split()[0] == url.split()[-1]:
		code = ''
		for tag in soup.findAll('html'):
			code += str(tag)
		with open('index.html', 'w') as html:
			html.write(code)

	else:
		if url.split()[1] == url.split()[-1]:
			for tag in soup.findAll(url.split()[1]):
				print(tag)
		else:
			for tag in soup.findAll(url.split()[1]):
				print(tag[url.split()[2]])
	print(l)

