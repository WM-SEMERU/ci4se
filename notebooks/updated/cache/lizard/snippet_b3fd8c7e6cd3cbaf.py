def refresh(self):
    self.clear()
    for i, filename in enumerate(self.filenames()):
        name = '%i. %s' % (i + 1, os.path.basename(filename))
        action = self.addAction(name)
        action.setData(wrapVariant(filename))