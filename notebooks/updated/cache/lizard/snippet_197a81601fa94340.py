def get_support_package(tile):
    packages = tile.find_products('support_package')
    if len(packages) == 0:
        return None
    elif len(packages) == 1:
        return packages[0]
    raise BuildError(
        'Tile declared multiple support packages, only one is supported',
        packages=packages)