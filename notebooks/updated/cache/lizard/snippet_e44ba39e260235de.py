def read_config_file(libname):
    filename = glymurrc_fname()
    if filename is None:
        return None
    parser = ConfigParser()
    parser.read(filename)
    try:
        path = parser.get('library', libname)
    except (NoOptionError, NoSectionError):
        path = None
    return path