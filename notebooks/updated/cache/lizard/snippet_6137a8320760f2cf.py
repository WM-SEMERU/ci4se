def archive_context(filename):
    tmpdir = tempfile.mkdtemp()
    log.warn('Extracting in %s', tmpdir)
    old_wd = os.getcwd()
    try:
        os.chdir(tmpdir)
        try:
            with ContextualZipFile(filename) as archive:
                archive.extractall()
        except zipfile.BadZipfile as err:
            if not err.args:
                err.args = '',
            err.args = err.args + (MEANINGFUL_INVALID_ZIP_ERR_MSG.format(
                filename),)
            raise
        subdir = os.path.join(tmpdir, os.listdir(tmpdir)[0])
        os.chdir(subdir)
        log.warn('Now working in %s', subdir)
        yield
    finally:
        os.chdir(old_wd)
        shutil.rmtree(tmpdir)