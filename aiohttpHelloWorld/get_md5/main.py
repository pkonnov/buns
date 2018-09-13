from aiohttp import web
import hashlib

async def index(request):
	return web.Response(text='no')

async def talk_url(request):
    summ = '100'
    id_u = '001'
    hash_md = hashlib.md5((summ + id_u).encode('utf-8')).hexdigest()
    return web.Response(text=hash_md)

app = web.Application()
app.add_routes([web.get('/', index),
                web.get('/uri?({hash_md})', talk_url)])

web.run_app(app)