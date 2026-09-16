def get_version(package_name, version_file='_version.py'):
    filename = os.path.join(os.path.dirname(__file__), package_name,
        version_file)
    with open(filename, 'rb') as fp:
        return fp.read().decode('utf8').split('=')[1].strip(" \n'")