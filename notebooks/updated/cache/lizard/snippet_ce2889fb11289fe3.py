def load(self, path=None, format=None, schema=None, **options):
    if format is not None:
        self.format(format)
    if schema is not None:
        self.schema(schema)
    self.options(**options)
    if path is not None:
        if type(path) != str or len(path.strip()) == 0:
            raise ValueError(
                'If the path is provided for stream, it needs to be a ' +
                'non-empty string. List of paths are not supported.')
        return self._df(self._jreader.load(path))
    else:
        return self._df(self._jreader.load())