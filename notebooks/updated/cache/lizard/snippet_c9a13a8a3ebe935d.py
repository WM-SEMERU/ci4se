def get_quantity(self, twig=None, unit=None, default=None, t=None, **kwargs):
    if default is not None is not None:
        if not len(self.filter(twig=twig, **kwargs)):
            return default
    param = self.get_parameter(twig=twig, **kwargs)
    if param.qualifier in kwargs.keys():
        return kwargs.get(param.qualifier)
    return param.get_quantity(unit=unit, t=t)