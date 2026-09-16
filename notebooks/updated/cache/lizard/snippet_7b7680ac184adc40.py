def save_global(self, verbose=False):
    self.save(os.path.expanduser(os.path.join('~', GLOBALCONFIG)), verbose)