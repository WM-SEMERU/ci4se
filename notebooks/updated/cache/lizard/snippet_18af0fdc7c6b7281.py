def _flatten_plus_safe(data_and_files):
    data, rollback_files = _normalize_args(data_and_files)
    with tx_tmpdir(data) as tmpdir:
        tx_files = [os.path.join(tmpdir, os.path.basename(f)) for f in
            rollback_files]
        yield tx_files, rollback_files