def version():
    path = join('lib', _CONFIG['name'], '__version__.py')
    with open(path) as stream:
        exec(stream.read())
    return __version__