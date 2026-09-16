def get_value(self, twig=None, unit=None, default=None, t=None, **kwargs):
    if default is not None:
        if not len(self.filter(twig=twig, **kwargs)):
            return default
    param = self.get_parameter(twig=twig, **kwargs)
    if isinstance(param, FloatParameter) or isinstance(param,
        FloatArrayParameter):
        return param.get_value(unit=unit, t=t, **kwargs)
    return param.get_value(**kwargs)