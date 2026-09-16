def bkg_noise(readout_noise, exposure_time, sky_brightness, pixel_scael,
    num_exposures=1):
    exposure_time_tot = num_exposures * exposure_time
    readout_noise_tot = num_exposures * readout_noise ** 2
    sky_per_pixel = sky_brightness * pixel_scael ** 2
    sigma_bkg = np.sqrt(readout_noise_tot + exposure_time_tot * 
        sky_per_pixel ** 2) / exposure_time_tot
    return sigma_bkg