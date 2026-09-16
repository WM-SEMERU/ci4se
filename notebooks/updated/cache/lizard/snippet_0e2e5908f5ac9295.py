def get_time(self):
    if isinstance(self.path, pathlib.Path):
        thetime = self.path.stat().st_mtime
    else:
        thetime = np.nan
    return thetime