def make_dirs(path):
    try:
        os.makedirs(os.path.dirname(path))
    except OSError as err:
        if err.errno != errno.EEXIST:
            LOGGER.error('Failed to create directory %s with error: %s' % (
                path, str(err)))
            raise