def _diff_archives(archive1, archive2, verbosity=0, interactive=True):
    if util.is_same_file(archive1, archive2):
        return 0
    diff = util.find_program('diff')
    if not diff:
        msg = (
            'The diff(1) program is required for showing archive differences, please install it.'
            )
        raise util.PatoolError(msg)
    tmpdir1 = util.tmpdir()
    try:
        path1 = _extract_archive(archive1, outdir=tmpdir1, verbosity=-1)
        tmpdir2 = util.tmpdir()
        try:
            path2 = _extract_archive(archive2, outdir=tmpdir2, verbosity=-1)
            return util.run_checked([diff, '-urN', path1, path2], verbosity
                =1, ret_ok=(0, 1))
        finally:
            shutil.rmtree(tmpdir2, onerror=rmtree_log_error)
    finally:
        shutil.rmtree(tmpdir1, onerror=rmtree_log_error)