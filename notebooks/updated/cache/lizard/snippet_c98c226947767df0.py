def charge_series(seq, granularity=0.1):
    if 'X' in seq:
        warnings.warn(_nc_warning_str, NoncanonicalWarning)
    ph_range = numpy.arange(1, 13, granularity)
    charge_at_ph = [sequence_charge(seq, ph) for ph in ph_range]
    return ph_range, charge_at_ph