def _save_file_and_pos(self):
    if not self._pos_changed:
        return
    with open(self.pos_storage_filename, 'w+') as f:
        _pos = '%s:%s' % (self._log_file, self._log_pos)
        _logger.debug('Saving position %s to file %s' % (_pos, self.
            pos_storage_filename))
        f.write(_pos)
        self._pos_changed = False