def open(self):
    self.vg.open()
    self.__pvh = lvm_pv_from_uuid(self.vg.handle, self.uuid)
    if not bool(self.__pvh):
        raise HandleError('Failed to initialize PV Handle.')