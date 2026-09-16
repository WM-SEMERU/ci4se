def validate_wave_unit(wave_unit):
    output_unit = validate_unit(wave_unit)
    unit_type = output_unit.physical_type
    if unit_type not in ('length', 'wavenumber', 'frequency'):
        raise exceptions.SynphotError(
            'wavelength physical type is not length, wave number, or frequency: {0}'
            .format(unit_type))
    return output_unit