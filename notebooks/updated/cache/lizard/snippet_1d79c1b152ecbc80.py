def walker(top, names):
    global packages, extensions
    if any(exc in top for exc in excludes):
        return
    package = top[top.rfind('holoviews'):].replace(os.path.sep, '.')
    packages.append(package)
    for name in names:
        ext = '.'.join(name.split('.')[1:])
        ext_str = '*.%s' % ext
        if ext and ext not in excludes and ext_str not in extensions[package]:
            extensions[package].append(ext_str)