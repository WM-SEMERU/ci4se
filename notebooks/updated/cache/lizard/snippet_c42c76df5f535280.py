def diff(self):
    self._copyfiles = False
    self._updatefiles = False
    self._purge = False
    self._creatdirs = False
    self._updatefiles = False
    self.log('Difference of directory %s from %s\n' % (self._dir2, self._dir1))
    self._diff(self._dir1, self._dir2)