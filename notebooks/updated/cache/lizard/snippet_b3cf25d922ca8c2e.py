def get_prefix():
    name = os.environ.get('NCLUSTER_PREFIX', DEFAULT_PREFIX)
    if name != DEFAULT_PREFIX:
        validate_prefix(name)
    return name