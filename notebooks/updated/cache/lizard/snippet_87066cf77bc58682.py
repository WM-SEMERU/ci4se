def close(self):
    if self.handle:
        q = lvm_quit(self.handle)
        if q != 0:
            raise HandleError('Failed to close LVM handle.')
        self.__handle = None