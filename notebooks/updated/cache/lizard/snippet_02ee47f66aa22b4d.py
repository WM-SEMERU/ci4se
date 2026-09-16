def _to_str(s):
    if sys.version_info[0] == 2 and not isinstance(s, str):
        return s.encode(sys.getfilesystemencoding())
    return s