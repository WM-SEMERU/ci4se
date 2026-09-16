def join_path(*components):
    if components:
        path = components[0]
        for next in components[1:]:
            path = win32.PathAppend(path, next)
    else:
        path = ''
    return path