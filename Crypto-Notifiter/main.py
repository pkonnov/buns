from bs4 import BeautifulSoup
import requests

def fetch_ethereum():
	url = "https://www.coingecko.com/en/price_charts/ethereum/usd"
	headers = {'User-Agent': 'Mozilla/5.0'}
	ethereum_file = request.get(url)


	soup = BeautifulSoup(ethereum_file.txt, 'html.parser')


	ethereum_li = []

	for table in soup.find_all('table', attrs={'class' : 'table table-responsive mt-2'}):
		for td in table.find_all('td'):
			ethereum_li.append(td.text)


	del ethereum_li[:3]


	ethereum_li = map(lambda s : s.strip(), ethereum_li)