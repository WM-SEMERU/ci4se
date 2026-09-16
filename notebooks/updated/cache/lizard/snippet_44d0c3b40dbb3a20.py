def ffl_path(self, site, frametype):
    try:
        return self.paths[site, frametype]
    except KeyError:
        self._find_paths()
        return self.paths[site, frametype]