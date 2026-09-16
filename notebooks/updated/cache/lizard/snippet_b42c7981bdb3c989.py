def is_blkdev(name):
    name = os.path.expanduser(name)
    stat_structure = None
    try:
        stat_structure = os.stat(name)
    except OSError as exc:
        if exc.errno == errno.ENOENT:
            return False
        else:
            raise
    return stat.S_ISBLK(stat_structure.st_mode)