from aiohttp import web
import jinja2
import aiohttp_jinja2
from get_md5.routes import setup_routes
from get_md5.settings import config

import argparse
import asyncio

try:
    import uvloop
    asyncio.set_event_loop_policy(uvloop.EventLoopPolicy)
except:
    print('_*_')

# deployment
parser = argparse.ArgumentParser(description="Demo project")
parser.add_argument('--host', help="Host to listen", default="localhost")
parser.add_argument('--port', help="Port to accept connections", default=8080)
parser.add_argument(
    '--reload',
    action="store_true",
    help="Autoreload code on change")
parser.add_argument("-c", "--config", type=argparse.FileType('r'),
                    help="Path to configuration file"
                    )

args = parser.parse_args()


# auto restart after changes
if args.reload:
    print("Start with code on change")
    import aioreloader
    aioreloader.start()


if __name__ == '__main__':
    app = web.Application()
    aiohttp_jinja2.setup(
        app,
        loader=jinja2.PackageLoader('get_md5', 'templates')
    )
    setup_routes(app)
    app['config'] = config
    web.run_app(app, host=args.host, port=args.port)