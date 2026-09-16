def run(cls, routes, *args, **kwargs):
    app = init(cls, routes, *args, **kwargs)
    HOST = os.getenv('HOST', '0.0.0.0')
    PORT = int(os.getenv('PORT', 8000))
    aiohttp.web.run_app(app, port=PORT, host=HOST)