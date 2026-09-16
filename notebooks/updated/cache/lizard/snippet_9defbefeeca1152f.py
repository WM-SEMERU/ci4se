def at(self, year, month, day):
    path = partial(_path, self.adapter)
    path = partial(path, int(year))
    path = partial(path, int(month))
    path = path(int(day))
    return self._get(path)