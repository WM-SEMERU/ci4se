def _get_adjustment(mag, year, mmin, completeness_year, t_f, mag_inc=0.1):
    if len(completeness_year) == 1:
        if mag >= mmin and year >= completeness_year[0]:
            return 1.0
        else:
            return False
    kval = int((mag - mmin) / mag_inc) + 1
    if kval >= 1 and year >= completeness_year[kval - 1]:
        return t_f
    else:
        return False