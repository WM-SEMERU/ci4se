def _abort_all_transfers(self, exception):
    pending_reads = len(self._commands_to_read)
    for transfer in self._transfer_list:
        transfer.add_error(exception)
    self._init_deferred_buffers()
    if isinstance(exception, DAPAccessIntf.TransferError):
        for _ in range(pending_reads):
            self._interface.read()