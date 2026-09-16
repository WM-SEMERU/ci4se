def _get_paths(self, fullname):
    real_path = os.path.join(*fullname[len(self.package_prefix):].split('.'))
    for base_path in sys.path:
        if base_path == '':
            base_path = os.getcwd()
        path = os.path.join(base_path, real_path)
        yield path + '.ipynb'
        yield path + '.py'
        yield os.path.join(path, '__init__.ipynb')
        yield os.path.join(path, '__init__.py')