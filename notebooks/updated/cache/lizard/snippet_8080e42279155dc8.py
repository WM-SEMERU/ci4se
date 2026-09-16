def _commandline(repositories, port=8000, host='127.0.0.1', debug=False,
    cache=None, cache_path='./cache', redis=None):
    if cache == 'redis':
        nautilus_cache = RedisCache(redis)
        cache_type = 'redis'
    elif cache == 'filesystem':
        nautilus_cache = FileSystemCache(cache_path)
        cache_type = 'simple'
    else:
        nautilus_cache = NullCache()
        cache_type = 'simple'
    app = Flask('Nautilus')
    if debug:
        app.logger.setLevel(logging.INFO)
    resolver = NautilusCtsResolver(resource=repositories)
    nautilus = FlaskNautilus(app=app, resolver=resolver)
    nautilus.resolver.parse()
    app.run(debug=debug, port=port, host=host)