def check_permission_safety(path):
    f_stats = os.stat(path)
    return f_stats.st_mode & (stat.S_IRWXG | stat.S_IRWXO
        ) == 0 and f_stats.st_uid == os.getuid()