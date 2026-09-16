def _is_unpacked_egg(path):
    return _is_egg_path(path) and os.path.isfile(os.path.join(path,
        'EGG-INFO', 'PKG-INFO'))