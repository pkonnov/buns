from aiohttp import web
import hashlib


async def talk_url(request):

    # /uri?sums=sums&id_u=id_u&param_hash=param_hash

    sums = request.rel_url.query['sums']
    id_u = request.rel_url.query['id_u']
    # hash_md = hashlib.md5((sums + id_u).encode('utf-8')).hexdigest()
    param_hash = request.rel_url.query['param_hash']
    params = "sums:{}, id_u:{}, hash:{}".format(sums, id_u, param_hash)
    return web.Response(text=str(params))
