def starmap(function, iterables, *args, **kwargs):
    return _map_or_starmap(function, iterables, args, kwargs, 'starmap')