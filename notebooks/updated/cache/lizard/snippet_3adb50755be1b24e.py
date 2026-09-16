def norm_slash(name):
    if isinstance(name, str):
        return name.replace('/', '\\') if not is_case_sensitive() else name
    else:
        return name.replace(b'/', b'\\') if not is_case_sensitive() else name