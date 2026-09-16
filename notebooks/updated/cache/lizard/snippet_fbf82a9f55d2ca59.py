def _diff(self, dir1, dir2):
    self._dcmp = self._compare(dir1, dir2)
    if self._dcmp.left_only:
        self.log('Only in %s' % dir1)
        for x in sorted(self._dcmp.left_only):
            self.log('>> %s' % x)
        self.log('')
    if self._dcmp.right_only:
        self.log('Only in %s' % dir2)
        for x in sorted(self._dcmp.right_only):
            self.log('<< %s' % x)
        self.log('')
    if self._dcmp.common:
        self.log('Common to %s and %s' % (self._dir1, self._dir2))
        for x in sorted(self._dcmp.common):
            self.log('-- %s' % x)
    else:
        self.log('No common files or sub-directories!')