def restore(self, res_id, backup_snap=None):
    name = self._get_name()
    out = self._cli.restore_snap(name, res_id, backup_snap)
    ex.raise_if_err(out, 'failed to restore snap {}.'.format(name), default
        =ex.VNXSnapError)