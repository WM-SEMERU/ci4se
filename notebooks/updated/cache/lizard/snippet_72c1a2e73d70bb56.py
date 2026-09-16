def find_config():
    cross_fs = 'SCUBA_DISCOVERY_ACROSS_FILESYSTEM' in os.environ
    path = os.getcwd()
    rel = ''
    while True:
        if os.path.exists(os.path.join(path, SCUBA_YML)):
            return path, rel
        if not cross_fs and os.path.ismount(path):
            msg = '{} not found here or any parent up to mount point {}'.format(SCUBA_YML, path) + """
Stopping at filesystem boundary (SCUBA_DISCOVERY_ACROSS_FILESYSTEM not set)."""
            raise ConfigNotFoundError(msg)
        path, rest = os.path.split(path)
        if not rest:
            raise ConfigNotFoundError(
                '{} not found here or any parent directories'.format(SCUBA_YML)
                )
        rel = os.path.join(rest, rel)