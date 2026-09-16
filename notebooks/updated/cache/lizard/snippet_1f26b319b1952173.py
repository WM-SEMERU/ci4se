def make_symlink(src_path, lnk_path):
    if CHECK_LUSTRE_PATH_LEN:
        src_path = patch_lustre_path(src_path)
        lnk_path = patch_lustre_path(lnk_path)
    if not os.path.exists(src_path):
        return
    try:
        os.symlink(src_path, lnk_path)
    except EnvironmentError as exc:
        if exc.errno != errno.EEXIST:
            raise
        elif not os.path.islink(lnk_path):
            print(
                'Warning: Cannot create symbolic link to {p}; a file named {f} already exists.'
                .format(p=src_path, f=lnk_path))
        elif os.path.realpath(lnk_path) != src_path:
            os.remove(lnk_path)
            os.symlink(src_path, lnk_path)