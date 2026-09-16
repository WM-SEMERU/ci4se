def _getTempFile(self, jobStoreID=None):
    if jobStoreID != None:
        self._checkJobStoreId(jobStoreID)
        return tempfile.mkstemp(suffix='.tmp', dir=os.path.join(self.
            _getAbsPath(jobStoreID), 'g'))
    else:
        return tempfile.mkstemp(prefix='tmp', suffix='.tmp', dir=self.
            _getTempSharedDir())