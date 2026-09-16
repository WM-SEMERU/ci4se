def run(self, t=None):
    r
    logger.info('―' * 80)
    logger.info('Running TransientTransport')
    if self.settings['t_scheme'] == 'steady':
        self[self.settings['quantity']] = 0.0
    try:
        self[self.settings['quantity']]
    except KeyError:
        self.set_IC(0)
    self._A_steady = self.A.copy()
    self._t_update_A()
    self._t_update_b()
    self._apply_BCs()
    self._A_t = self._A.copy()
    self._b_t = self._b.copy()
    if t is None:
        t = self.settings['t_initial']
    self._update_physics()
    self._run_transient(t=t)