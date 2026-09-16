def inject_config(self, config, from_args):
    load_libs = self._get_libs()
    all_libs = {}
    found_libs = []
    for root, dirs, files in os.walk(library_path):
        for f in files:
            if not f.endswith('.so'):
                continue
            full_path = os.path.join(root, f)
            if '.' in f:
                name, ext = f.split('.', 1)
            else:
                name = f
            if name in all_libs:
                all_libs[name].append(full_path)
            else:
                all_libs[name] = [full_path]
    for lib in load_libs:
        if 'lib' + lib in all_libs:
            p = list(sorted(all_libs['lib' + lib], key=lambda x: len(x))).pop()
            v = '--volume={0}:{1}'.format(os.path.realpath(p), p)
            config.append(v)
        else:
            print('*** Unknown lib: {}'.format(lib))
            sys.exit(1)