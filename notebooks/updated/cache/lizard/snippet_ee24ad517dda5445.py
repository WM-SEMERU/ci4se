def non_existing_path(path_, dpath=None, offset=0, suffix=None, force_fmt=False
    ):
    r
    import utool as ut
    from os.path import basename, dirname
    if dpath is None:
        dpath = dirname(path_)
    base_fmtstr = basename(path_)
    if suffix is not None:
        base_fmtstr = ut.augpath(base_fmtstr, suffix)
    if '%' not in base_fmtstr:
        if not force_fmt:
            first_choice = join(dpath, base_fmtstr)
            if not exists(first_choice):
                return first_choice
        base_fmtstr = ut.augpath(base_fmtstr, '%d')
    dname_list = ut.glob(dpath, pattern='*', recursive=False, with_files=
        True, with_dirs=True)
    conflict_set = set(basename(dname) for dname in dname_list)
    newname = ut.get_nonconflicting_string(base_fmtstr, conflict_set,
        offset=offset)
    newpath = join(dpath, newname)
    return newpath