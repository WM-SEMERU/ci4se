def rm(path, isdir=False):
    if isdir:
        deleted = os.path.isdir(path)
        shutil.rmtree(path, ignore_errors=True)
    elif os.path.isfile(path) or os.path.islink(path):
        deleted = True
        os.remove(path)
    else:
        deleted = False
    return deleted