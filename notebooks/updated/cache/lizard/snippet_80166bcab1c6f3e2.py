def _convert_to_from(self, to_mag, from_mag, fromVMag=None):
    lumtype = self.spectral_type.lumType
    specClass = self.spectral_type.roundedSpecClass
    if not specClass:
        raise ValueError('Can not convert when no spectral class is given')
    if lumtype not in ('V', ''):
        raise ValueError(
            'Can only convert for main sequence stars. Got {0} type'.format
            (lumtype))
    if to_mag == 'V':
        col, sign = self.column_for_V_conversion[from_mag]
        try:
            offset = float(magDict[specClass][col])
        except KeyError:
            raise ValueError(
                'No data available to convert those magnitudes for that spectral type'
                )
        if math.isnan(offset):
            raise ValueError(
                'No data available to convert those magnitudes for that spectral type'
                )
        else:
            from_mag_val = self.__dict__['mag' + from_mag]
            if isNanOrNone(from_mag_val):
                raise ValueError(
                    'You cannot convert from a magnitude you have not specified in class'
                    )
            return from_mag_val + offset * sign
    elif from_mag == 'V':
        if fromVMag is None:
            raise ValueError('Must give fromVMag, even if it is self.magV')
        col, sign = self.column_for_V_conversion[to_mag]
        try:
            offset = float(magDict[specClass][col])
        except KeyError:
            raise ValueError(
                'No data available to convert those magnitudes for that spectral type'
                )
        if math.isnan(offset):
            raise ValueError(
                'No data available to convert those magnitudes for that spectral type'
                )
        else:
            return fromVMag + offset * sign * -1
    else:
        raise ValueError(
            'Can only convert from and to V magnitude. Use .convert() instead')