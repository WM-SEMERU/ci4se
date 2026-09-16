def dir(suffix='', prefix='tmp', dir=None, force=True):
    name = tempfile.mkdtemp(suffix, prefix, dir)
    try:
        yield name
    finally:
        try:
            if force:
                shutil.rmtree(name)
            else:
                os.rmdir(name)
        except OSError as e:
            if e.errno != 2:
                raise