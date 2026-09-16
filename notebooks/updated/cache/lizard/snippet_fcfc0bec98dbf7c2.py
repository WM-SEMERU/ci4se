def get_files_by_path(path):
    if os.path.isfile(path):
        return [path]
    if os.path.isdir(path):
        return get_morph_files(path)
    raise IOError('Invalid data path %s' % path)