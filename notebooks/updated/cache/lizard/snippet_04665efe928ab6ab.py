def find_jar(jar_name, root_path=None):
    jar_name = os.path.basename(jar_name)
    root = root_path or os.getcwd()
    paths = root, os.path.join(root, 'build'), '/usr/share/java'
    for p in paths:
        p = os.path.join(p, jar_name)
        if os.path.exists(p):
            return p
    return None