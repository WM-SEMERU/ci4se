def StartGdb(self):
    if self.attached:
        raise GdbProcessError('Gdb is already running.')
    self._gdb = GdbProxy(arch=self.arch)
    self._gdb.Attach(self.position)
    if self.auto_symfile_loading:
        try:
            self.LoadSymbolFile()
        except (ProxyError, TimeoutError) as err:
            self._gdb = GdbProxy(arch=self.arch)
            self._gdb.Attach(self.position)
            if not self.gdb.IsSymbolFileSane(self.position):
                logging.warning(
                    'Failed to automatically load a sane symbol file, most functionality will be unavailable until symbolfile is provided.'
                    )
                logging.debug(err.message)