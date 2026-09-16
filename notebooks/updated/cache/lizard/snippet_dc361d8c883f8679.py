def kwargs2args(self, kwargs_lens=None, kwargs_source=None,
    kwargs_lens_light=None, kwargs_ps=None, kwargs_cosmo=None):
    args = self.lensParams.setParams(kwargs_lens)
    args += self.souceParams.setParams(kwargs_source)
    args += self.lensLightParams.setParams(kwargs_lens_light)
    args += self.pointSourceParams.setParams(kwargs_ps)
    args += self.cosmoParams.setParams(kwargs_cosmo)
    return args