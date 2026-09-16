def disc(ghi, solar_zenith, datetime_or_doy, pressure=101325,
    min_cos_zenith=0.065, max_zenith=87, max_airmass=12):
    I0 = get_extra_radiation(datetime_or_doy, 1370.0, 'spencer')
    kt = clearness_index(ghi, solar_zenith, I0, min_cos_zenith=
        min_cos_zenith, max_clearness_index=1)
    am = atmosphere.get_relative_airmass(solar_zenith, model='kasten1966')
    if pressure is not None:
        am = atmosphere.get_absolute_airmass(am, pressure)
    Kn, am = _disc_kn(kt, am, max_airmass=max_airmass)
    dni = Kn * I0
    bad_values = (solar_zenith > max_zenith) | (ghi < 0) | (dni < 0)
    dni = np.where(bad_values, 0, dni)
    output = OrderedDict()
    output['dni'] = dni
    output['kt'] = kt
    output['airmass'] = am
    if isinstance(datetime_or_doy, pd.DatetimeIndex):
        output = pd.DataFrame(output, index=datetime_or_doy)
    return output