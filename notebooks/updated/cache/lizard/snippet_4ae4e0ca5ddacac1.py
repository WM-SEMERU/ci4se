def is_str(string):
    if sys.version_info[:2] >= (3, 0):
        return isinstance(string, str)
    return isinstance(string, basestring)