def pretty_path(path, _home_re=re.compile('^' + re.escape(os.path.
    expanduser('~') + os.sep))):
    path = format_filename(path)
    path = _home_re.sub('~' + os.sep, path)
    return path