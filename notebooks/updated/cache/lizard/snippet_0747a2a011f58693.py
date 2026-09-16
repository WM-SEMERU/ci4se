def temp_chdir(cwd=None):
    if six.PY3:
        from tempfile import TemporaryDirectory
        with TemporaryDirectory() as tempwd:
            origin = cwd or os.getcwd()
            os.chdir(tempwd)
            try:
                yield tempwd if os.path.exists(tempwd) else ''
            finally:
                os.chdir(origin)
    else:
        from tempfile import mkdtemp
        tempwd = mkdtemp()
        origin = cwd or os.getcwd()
        os.chdir(tempwd)
        try:
            yield tempwd if os.path.exists(tempwd) else ''
        finally:
            os.chdir(origin)