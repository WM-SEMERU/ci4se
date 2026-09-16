def list_files(dir_pathname, recursive=True, topdown=True, followlinks=False):
    for root, dirnames, filenames in walk(dir_pathname, recursive, topdown,
        followlinks):
        for filename in filenames:
            yield absolute_path(os.path.join(root, filename))