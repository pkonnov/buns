#!/usr/bin/python3
from aiohttp import web
import hashlib


async def talk_url(request):
	summ = '100'
	id_u = '001'
	q = '?'
	hash_md = hashlib.md5((summ + id_u).encode('utf-8')).hexdigest()
	return web.Response(text=hash_md)

app = web.Application()
app.router.add_route('GET', '/uri?sum={summ}&id={id_u}&hash={hash_md}', talk_url)


if __name__ == '__main__':
	web.run_app(app)
