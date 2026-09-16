def get_template(name):
    path = pkg_resources.resource_filename('vr.runners', 'templates/' + name)
    with open(path, 'r') as f:
        return f.read()