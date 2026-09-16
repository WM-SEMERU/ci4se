def _open_for_csv(name, mode):
    if sys.version_info[0] < 3:
        return open_rw(name, mode + 'b')
    return open_rw(name, mode, newline='', encoding='utf-8')