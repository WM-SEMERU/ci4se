def make_strain_from_inj_object(self, inj, delta_t, detector_name, f_lower=
    None, distance_scale=1):
    detector = Detector(detector_name)
    if f_lower is None:
        f_l = inj.f_lower
    else:
        f_l = f_lower
    hp, hc = get_td_waveform(inj, delta_t=delta_t, f_lower=f_l, **self.
        extra_args)
    hp /= distance_scale
    hc /= distance_scale
    hp._epoch += inj.tc
    hc._epoch += inj.tc
    try:
        hp_tapered = wfutils.taper_timeseries(hp, inj.taper)
        hc_tapered = wfutils.taper_timeseries(hc, inj.taper)
    except AttributeError:
        hp_tapered = hp
        hc_tapered = hc
    signal = detector.project_wave(hp_tapered, hc_tapered, inj.ra, inj.dec,
        inj.polarization)
    return signal