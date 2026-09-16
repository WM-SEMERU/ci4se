def candidate_paths(self, filepath):
    filelead, filetail = os.path.split(filepath)
    name, extension = os.path.splitext(filetail)
    if extension:
        extension = extension[1:]
    filenames = [name]
    if not name.startswith('_'):
        filenames.append('_{}'.format(name))
    if extension and extension in self.CANDIDATE_EXTENSIONS:
        filenames = ['.'.join([k, extension]) for k in filenames]
    else:
        if extension:
            filenames = ['.'.join([k, extension]) for k in filenames]
        new = []
        for ext in self.CANDIDATE_EXTENSIONS:
            new.extend(['.'.join([k, ext]) for k in filenames])
        filenames = new
    return [os.path.join(filelead, v) for v in filenames]