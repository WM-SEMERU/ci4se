def remove_file(filename, path=None):
    cwd = os.getcwd()
    try:
        if path:
            os.chdir(path)
    except OSError:
        raise
    try:
        os.remove(filename)
        os.chdir(cwd)
        return True
    except OSError:
        os.chdir(cwd)
        raise