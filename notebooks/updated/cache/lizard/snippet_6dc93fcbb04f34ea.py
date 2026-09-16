def make_map():
    map = Mapper(directory=config['pylons.paths']['controllers'],
        always_scan=config['debug'])
    map.connect('error/:action/:id', controller='error')
    map.connect(':controller/:action/:id')
    return map