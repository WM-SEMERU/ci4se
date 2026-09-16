def calculate_lyapunov(self):
    if self._calculate_megno == 0:
        raise RuntimeError(
            'Lyapunov Characteristic Number cannot be calculated. Make sure to call init_megno() after adding all particles but before integrating the simulation.'
            )
    clibrebound.reb_tools_calculate_lyapunov.restype = c_double
    return clibrebound.reb_tools_calculate_lyapunov(byref(self))