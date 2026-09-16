def fetchAfterStateFile(self, file_folder):
    if 'true' == self.after:
        self.log.info('This file has been deleted successfully.')
    else:
        self.log.info('Fetching final file of this Change<%s>:' % self)
        return self._fetchFile(self.after, file_folder)