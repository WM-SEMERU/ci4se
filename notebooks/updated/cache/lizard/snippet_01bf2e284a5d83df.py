def diffusion_driver(self):
    if self._diffusion_driver is None:
        return self,
    if isinstance(self._diffusion_driver, list):
        return tuple(self._diffusion_driver)
    if isinstance(self._diffusion_driver, tuple):
        return self._diffusion_driver
    return self._diffusion_driver,