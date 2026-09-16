def is_writable_dir(directory, **kwargs):
    try:
        testfile = tempfile.TemporaryFile(dir=directory)
        testfile.close()
    except OSError as e:
        if e.errno == errno.EACCES:
            return False
        elif e.errno == errno.ENOENT:
            if kwargs.get('mkdir') == True:
                try:
                    os.makedirs(directory)
                except OSError as e2:
                    if e2.errno == errno.EACCES:
                        return False
            else:
                return False
        e.filename = directory
    return True