def get_package_class_name(name):
    if name[0] != 'L' and name[-1] != ';':
        raise ValueError("The name '{}' does not look like a typed name!".
            format(name))
    name = name[1:-1]
    if '/' not in name:
        return '', name
    package, clsname = name.rsplit('/', 1)
    package = package.replace('/', '.')
    return package, clsname