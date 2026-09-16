def set_hostname(self, hostname):
    self.oem_init()
    try:
        return self._oem.set_hostname(hostname)
    except exc.UnsupportedFunctionality:
        return self.set_mci(hostname)