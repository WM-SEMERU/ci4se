def saveto(self, path, sortkey=True):
    with open(path, 'w') as f:
        self.savetofile(f, sortkey)