def from_stat_file(cls, statfile, timestep=1, is_leap_year=False):
    stat = STAT(statfile)

    def check_missing(opt_data, data_name):
        if opt_data == []:
            raise ValueError('Stat file contains no optical data.')
        for i, x in enumerate(opt_data):
            if x is None:
                raise ValueError(
                    'Missing optical depth data for {} at month {}'.format(
                    data_name, i))
    check_missing(stat.monthly_tau_beam, 'monthly_tau_beam')
    check_missing(stat.monthly_tau_diffuse, 'monthly_tau_diffuse')
    return cls.from_ashrae_revised_clear_sky(stat.location, stat.
        monthly_tau_beam, stat.monthly_tau_diffuse, timestep, is_leap_year)