from views import talk_url


def setup_routes(app):
    app.router.add_route('GET', "/uri", talk_url)