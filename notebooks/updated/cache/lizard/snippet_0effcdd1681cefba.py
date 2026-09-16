def reindl(surface_tilt, surface_azimuth, dhi, dni, ghi, dni_extra,
    solar_zenith, solar_azimuth):
    r
    cos_tt = aoi_projection(surface_tilt, surface_azimuth, solar_zenith,
        solar_azimuth)
    cos_tt = np.maximum(cos_tt, 0)
    cos_solar_zenith = tools.cosd(solar_zenith)
    Rb = cos_tt / np.maximum(cos_solar_zenith, 0.01745)
    AI = dni / dni_extra
    HB = dni * cos_solar_zenith
    HB = np.maximum(HB, 0)
    term1 = 1 - AI
    term2 = 0.5 * (1 + tools.cosd(surface_tilt))
    term3 = 1 + np.sqrt(HB / ghi) * tools.sind(0.5 * surface_tilt) ** 3
    sky_diffuse = dhi * (AI * Rb + term1 * term2 * term3)
    sky_diffuse = np.maximum(sky_diffuse, 0)
    return sky_diffuse