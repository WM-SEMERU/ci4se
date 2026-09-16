def add(self, origin):
    digest = self._calc_digest(origin)
    if self.exists(digest):
        self.logger.debug(
            'Added File: [{0}] ( Already exists. Skipping transfer)'.format
            (digest))
        return digest
    absPath = self.get_file_path(digest)
    absFolderPath = os.path.dirname(absPath)
    self._makedirs(absFolderPath)
    self._copy_content(origin, absPath)
    self.logger.debug('Added file: "{0}" [{1}]'.format(digest, absPath))
    return digest