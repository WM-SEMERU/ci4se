def _get_datetimes(timestep, is_leap_year):
    hour_count = 8760 + 24 if is_leap_year else 8760
    adjust_time = 30 if timestep == 1 else 0
    return tuple(DateTime.from_moy(60.0 * count / timestep + adjust_time,
        is_leap_year) for count in xrange(hour_count * timestep))