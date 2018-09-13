from aiohttp import web
import hashlib

routes = web.RouteTableDef()

@routes.get('/uri?sum={summ}&id={id_user}')
async def take_url(request):
 	summ = '100'
 	id_user = '001'
 	hash_sum = summ + id_user
 	hash_md = hashlib.md5(hash_sum.encode('utf-8')).hexdigest()
 	return web.Response(text=hash_md)


#site/uri?sum=100&id=001&hash=e2a6a1ace352668000aed191a817d143
