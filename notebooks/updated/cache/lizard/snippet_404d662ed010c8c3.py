def tx_tmpdir(base_dir, rollback_dirpath):
    if exists(rollback_dirpath):
        critical(rollback_dirpath + ' already exists')
    tmp_dir = tempfile.mkdtemp(dir=base_dir)
    safe_mkdir(tmp_dir)
    try:
        yield tmp_dir
    finally:
        if tmp_dir and exists(tmp_dir):
            os.rename(tmp_dir, rollback_dirpath)