def glob(dpath, pattern=None, recursive=False, with_files=True, with_dirs=
    True, maxdepth=None, exclude_dirs=[], fullpath=True, **kwargs):
    r
    gen = iglob(dpath, pattern, recursive=recursive, with_files=with_files,
        with_dirs=with_dirs, maxdepth=maxdepth, fullpath=fullpath,
        exclude_dirs=exclude_dirs, **kwargs)
    path_list = list(gen)
    return path_list