def save(self, filename=None, directory=None):
    if filename is not None:
        self.filename = filename
    if directory is not None:
        self.directory = directory
    filepath = self.filepath
    tools.mkdirs(filepath)
    data = text_type(self.source)
    with io.open(filepath, 'w', encoding=self.encoding) as fd:
        fd.write(data)
        if not data.endswith('\n'):
            fd.write('\n')
    return filepath