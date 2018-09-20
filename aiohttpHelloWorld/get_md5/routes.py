from .views import *


def setup_routes(app):
    app.router.add_route('GET', "/uri", talk_url)
    app.router.add_route('GET', '/', index)

