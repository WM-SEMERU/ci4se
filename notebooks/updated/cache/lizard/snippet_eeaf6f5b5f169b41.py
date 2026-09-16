def match(self, files):
    if self.include is not None:
        for path in files:
            if self.regex.match(path) is not None:
                yield path