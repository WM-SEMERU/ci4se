def open_tar(path_or_file, *args, **kwargs):
    path, fileobj = (path_or_file, None) if isinstance(path_or_file,
        string_types) else (None, path_or_file)
    with closing(TarFile.open(path, *args, fileobj=fileobj, **kwargs)) as tar:
        yield tar