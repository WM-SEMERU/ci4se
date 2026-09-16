def unpack(src_dir, dst_dir):
    for dirpath, dirnames, filenames in os.walk(src_dir):
        subdir = os.path.relpath(dirpath, src_dir)
        for f in filenames:
            src = os.path.join(dirpath, f)
            dst = os.path.join(dst_dir, subdir, f)
            os.renames(src, dst)
        for n, d in reversed(list(enumerate(dirnames))):
            src = os.path.join(dirpath, d)
            dst = os.path.join(dst_dir, subdir, d)
            if not os.path.exists(dst):
                os.renames(src, dst)
                del dirnames[n]
    for dirpath, dirnames, filenames in os.walk(src_dir, topdown=True):
        assert not filenames
        os.rmdir(dirpath)