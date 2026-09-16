def _clean_dir(root, keep, exclude_pat):
    root = os.path.normcase(root)
    real_keep = _find_keep_files(root, keep)
    removed = set()

    def _delete_not_kept(nfn):
        if nfn not in real_keep:
            if not salt.utils.stringutils.check_include_exclude(os.path.
                relpath(nfn, root), None, exclude_pat):
                return
            removed.add(nfn)
            if not __opts__['test']:
                try:
                    os.remove(nfn)
                except OSError:
                    __salt__['file.remove'](nfn)
    for roots, dirs, files in salt.utils.path.os_walk(root):
        for name in itertools.chain(dirs, files):
            _delete_not_kept(os.path.join(roots, name))
    return list(removed)