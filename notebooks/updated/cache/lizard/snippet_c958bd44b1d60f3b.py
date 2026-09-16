def unmount_loopbacks(self):
    self._index_loopbacks()
    for dev in self.find_loopbacks():
        _util.check_output_(['losetup', '-d', dev])