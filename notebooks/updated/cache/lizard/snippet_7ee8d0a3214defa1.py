def group_by_month(self):
    hourly_data_by_month = OrderedDict()
    for d in xrange(1, 13):
        hourly_data_by_month[d] = []
    a_per = self.header.analysis_period
    a_per_months = a_per.months_int
    indx = 24 * a_per.timestep * abs(a_per.st_day - 1 - a_per.
        _num_of_days_each_month[a_per_months[0] - 1])
    hourly_data_by_month[a_per_months[0]] = self._values[0:indx + 1]
    if len(a_per_months) > 1:
        for mon in a_per_months[1:]:
            interval = a_per._num_of_days_each_month[mon - 1
                ] * 24 * a_per.timestep
            try:
                hourly_data_by_month[mon] = self._values[indx:indx +
                    interval + 1]
            except IndexError:
                hourly_data_by_month[mon] = self._values[indx:]
            indx += interval
    return hourly_data_by_month