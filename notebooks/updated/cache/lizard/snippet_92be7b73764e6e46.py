def bump_minor_version():
    version = load_version_as_list()
    print('current version: {}'.format(format_version_string(version)))
    version[-1] += 1
    print('new version: {}'.format(format_version_string(version)))
    contents = "__version__ = '{}'\n".format(format_version_string(version))
    with open(VERSION_PATH, 'w') as wfile:
        wfile.write(contents)