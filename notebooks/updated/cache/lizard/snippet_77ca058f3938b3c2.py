def _ensure_dir_exists(path):
    if not op.exists(path):
        os.makedirs(path)
    assert op.exists(path) and op.isdir(path)