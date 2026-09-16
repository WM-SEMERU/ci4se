def jtag_enable(self):
    status, _ = self.bulkCommand(_BMSG_ENABLE_JTAG)
    if status == 0:
        self._jtagon = True
    elif status == 3:
        self._jtagon = True
        raise JTAGAlreadyEnabledError()
    else:
        raise JTAGEnableFailedError('Error enabling JTAG. Error code: %s.' %
            status)