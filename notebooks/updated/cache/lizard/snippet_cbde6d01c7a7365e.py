def _directory_import(self):
    path = os.path.abspath(self.path)
    ws = pkg_resources.WorkingSet([])
    ws.add_entry(path)
    dist = ws.by_key.get(DIST_NAME)
    if dist is None:
        setup_py = os.path.join(path, 'setup.py')
        if os.path.isfile(setup_py):
            sp.check_output([sys.executable, 'setup.py', 'egg_info'], cwd=path)
            for dist in pkg_resources.find_distributions(path, True):
                return dist
    return dist