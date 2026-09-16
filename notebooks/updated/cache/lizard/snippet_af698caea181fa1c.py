def get_subpackages(name):
    splist = []
    for dirpath, _dirnames, _filenames in os.walk(name):
        if osp.isfile(osp.join(dirpath, '__init__.py')):
            splist.append('.'.join(dirpath.split(os.sep)))
    return splist