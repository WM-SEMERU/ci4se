def index_modules(idx=None, path=None):
    suppress_output()
    modules = defaultdict(list)
    pkglist = pkgutil.walk_packages(onerror=lambda x: True)
    print(pkglist)
    if path:
        pkglist = pkgutil.walk_packages(path, onerror=lambda x: True)
    for modl, name, ispkg in pkglist:
        try:
            path = os.path.join(modl.path, name.split('.')[-1])
        except AttributeError:
            continue
        if os.path.isdir(path):
            path = os.path.join(path, '__init__')
        path += '.py'
        objs = []
        if os.path.exists(path):
            try:
                objs = read_objs_from_path(path)
            except:
                continue
        elif not re.search(MODULE_BLACKLIST, name):
            try:
                mod = __import__(name)
                objs = [k for k in dir(mod) if not k.startswith('__')]
            except:
                continue
        else:
            continue
        for obj in objs:
            if name not in modules[obj]:
                modules[obj].append(name)
    suppress_output(True)
    return merge_dicts(idx, dict(modules))