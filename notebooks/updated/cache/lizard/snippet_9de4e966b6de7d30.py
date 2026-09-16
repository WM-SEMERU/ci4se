def temporary_dir(root_dir=None, cleanup=True, suffix='', permissions=None,
    prefix=tempfile.template):
    path = tempfile.mkdtemp(dir=root_dir, suffix=suffix, prefix=prefix)
    try:
        if permissions is not None:
            os.chmod(path, permissions)
        yield path
    finally:
        if cleanup:
            shutil.rmtree(path, ignore_errors=True)