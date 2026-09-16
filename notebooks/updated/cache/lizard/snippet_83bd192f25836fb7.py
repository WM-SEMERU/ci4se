def check_gsims(self, gsims):
    imts = set(from_string(imt).name for imt in self.imtls)
    for gsim in gsims:
        restrict_imts = gsim.DEFINED_FOR_INTENSITY_MEASURE_TYPES
        if restrict_imts:
            names = set(cls.__name__ for cls in restrict_imts)
            invalid_imts = ', '.join(imts - names)
            if invalid_imts:
                raise ValueError(
                    'The IMT %s is not accepted by the GSIM %s' % (
                    invalid_imts, gsim))
        if 'site_model' not in self.inputs:
            for param in gsim.REQUIRES_SITES_PARAMETERS:
                if param in ('lon', 'lat'):
                    continue
                param_name = self.siteparam[param]
                param_value = getattr(self, param_name)
                if isinstance(param_value, float) and numpy.isnan(param_value):
                    raise ValueError(
                        'Please set a value for %r, this is required by the GSIM %s'
                         % (param_name, gsim))