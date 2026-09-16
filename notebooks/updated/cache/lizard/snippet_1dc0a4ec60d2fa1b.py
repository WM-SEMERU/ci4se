def _filter(self, filename):
    return self.name_filter is not None and re.search(self.name_filter,
        filename) is None