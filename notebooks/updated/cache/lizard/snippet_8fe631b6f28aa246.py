def _write_config(self, cfg, slot):
    old_pgm_seq = self._status.pgm_seq
    frame = cfg.to_frame(slot=slot)
    self._debug('Writing %s frame :\n%s\n' % (yubikey_config.command2str(
        frame.command), cfg))
    self._write(frame)
    self._waitfor_clear(yubikey_defs.SLOT_WRITE_FLAG)
    self.status()
    self._debug('Programmed slot %i, sequence %i -> %i\n' % (slot,
        old_pgm_seq, self._status.pgm_seq))
    cfgs = self._status.valid_configs()
    if not cfgs and self._status.pgm_seq == 0:
        return
    if self._status.pgm_seq == old_pgm_seq + 1:
        return
    raise YubiKeyUSBHIDError(
        'YubiKey programming failed (seq %i not increased (%i))' % (
        old_pgm_seq, self._status.pgm_seq))