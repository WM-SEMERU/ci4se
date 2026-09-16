def chmod_and_retry(func, path, exc_info):
    if func is os.listdir or os.name != 'nt':
        raise
    os.chmod(path, stat.S_IREAD | stat.S_IWRITE)
    func(path)