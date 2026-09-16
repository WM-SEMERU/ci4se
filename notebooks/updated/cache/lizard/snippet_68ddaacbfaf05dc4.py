def init_path():
    sitedirs = getsyssitepackages()
    for sitedir in sitedirs:
        env_path = os.environ['PATH'].split(os.pathsep)
        for module in allowed_modules:
            p = join(sitedir, module)
            if isdir(p) and not p in env_path:
                os.environ['PATH'] += env_t(os.pathsep + p)