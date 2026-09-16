def _pre_commit(files, options):
    errors = []
    tmpdir = mkdtemp()
    files_to_check = []
    try:
        for file_, content in files:
            dirname, filename = os.path.split(os.path.abspath(file_))
            prefix = os.path.commonprefix([dirname, tmpdir])
            dirname = os.path.relpath(dirname, start=prefix)
            dirname = os.path.join(tmpdir, dirname)
            if not os.path.isdir(dirname):
                os.makedirs(dirname)
            filename = os.path.join(dirname, filename)
            with open(filename, 'wb') as fh:
                fh.write(content)
            files_to_check.append((file_, filename))
        for file_, filename in files_to_check:
            errors += list(map(lambda x: '{0}: {1}'.format(file_, x), 
                check_file(filename, **options) or []))
    finally:
        shutil.rmtree(tmpdir, ignore_errors=True)
    return errors