def _convert_rename(self, fc):
    old = fc.old_path
    new = fc.new_path
    keep_old = self._path_to_be_kept(old)
    keep_new = self._path_to_be_kept(new)
    if keep_old and keep_new:
        fc.old_path = self._adjust_for_new_root(old)
        fc.new_path = self._adjust_for_new_root(new)
        return fc
    elif keep_old:
        old = self._adjust_for_new_root(old)
        return commands.FileDeleteCommand(old)
    elif keep_new:
        self.warning('cannot turn rename of %s into an add of %s yet' % (
            old, new))
    return None