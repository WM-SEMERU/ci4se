def select(self, versions):
    options = list(self.filter(versions))
    if options:
        return max(options)
    return None