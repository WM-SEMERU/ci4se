def get_filenames(root, prefix='', suffix=''):
    return [fnm for fnm in os.listdir(root) if fnm.startswith(prefix) and
        fnm.endswith(suffix)]