def _add_write_pbs(self, write_pbs):
    if self._read_only:
        raise ValueError(_WRITE_READ_ONLY)
    super(Transaction, self)._add_write_pbs(write_pbs)