def get_subpath(self, subpath: str):
    for d in self._path:
        if os.path.exists(os.path.join(d, subpath)):
            return os.path.join(d, subpath)
    raise FileNotFoundError