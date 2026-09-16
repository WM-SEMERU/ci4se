def fit(self, vxvv, vxvv_err=None, pot=None, radec=False, lb=False,
    customsky=False, lb_to_customsky=None, pmllpmbb_to_customsky=None,
    tintJ=10, ntintJ=1000, integrate_method='dopr54_c', disp=False, **kwargs):
    if pot is None:
        try:
            pot = self._pot
        except AttributeError:
            raise AttributeError('Integrate orbit first or specify pot=')
    if radec or lb or customsky:
        obs, ro, vo = self._parse_radec_kwargs(kwargs, vel=True, dontpop=True)
    else:
        obs, ro, vo = None, None, None
    if customsky and (lb_to_customsky is None or pmllpmbb_to_customsky is None
        ):
        raise IOError(
            'if customsky=True, the functions lb_to_customsky and pmllpmbb_to_customsky need to be given'
            )
    new_vxvv, maxLogL = _fit_orbit(self, vxvv, vxvv_err, pot, radec=radec,
        lb=lb, customsky=customsky, lb_to_customsky=lb_to_customsky,
        pmllpmbb_to_customsky=pmllpmbb_to_customsky, tintJ=tintJ, ntintJ=
        ntintJ, integrate_method=integrate_method, ro=ro, vo=vo, obs=obs,
        disp=disp)
    self.vxvv = new_vxvv
    return maxLogL