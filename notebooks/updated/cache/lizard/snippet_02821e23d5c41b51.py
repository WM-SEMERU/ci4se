def _build_paths():
    paths = sysconfig.get_paths()
    return {'prefix': sys.prefix, 'data': paths['data'], 'scripts': paths[
        'scripts'], 'headers': paths['include'], 'purelib': paths['purelib'
        ], 'platlib': paths['platlib']}