def _find_files(self):
    files = []
    for ext in self.extensions:
        ext_files = util.find_files(self.root, '*' + ext)
        log.debug("found {} '*{}' files in '{}'".format(len(ext_files), ext,
            self.root))
        files.extend(ext_files)
    return files