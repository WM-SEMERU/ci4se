def _calc_dir_size(path):
    dir_size = 0
    for root, dirs, files in os.walk(path):
        for fn in files:
            full_fn = os.path.join(root, fn)
            dir_size += os.path.getsize(full_fn)
    return dir_size