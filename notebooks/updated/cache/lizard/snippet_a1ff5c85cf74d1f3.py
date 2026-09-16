def inject_nmi(self):
    cur_status = self.get_host_power_status()
    if cur_status != 'ON':
        raise exception.IloError('Server is not in powered on state.')
    self._perform_power_op('Nmi')