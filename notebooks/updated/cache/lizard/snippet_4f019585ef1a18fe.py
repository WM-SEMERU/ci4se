def signature(f, s=None, block_size=RS_DEFAULT_BLOCK_LEN):
    if s is None:
        s = tempfile.SpooledTemporaryFile(max_size=MAX_SPOOL, mode='wb+')
    job = _librsync.rs_sig_begin(block_size, RS_DEFAULT_STRONG_LEN)
    try:
        _execute(job, f, s)
    finally:
        _librsync.rs_job_free(job)
    return s