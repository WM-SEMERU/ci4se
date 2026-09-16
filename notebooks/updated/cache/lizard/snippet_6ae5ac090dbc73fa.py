def group_by_month_per_hour(self):
    data_by_month_per_hour = OrderedDict()
    for m in xrange(1, 13):
        for h in xrange(0, 24):
            data_by_month_per_hour[m, h] = []
    for v, dt in zip(self.values, self.datetimes):
        data_by_month_per_hour[dt.month, dt.hour].append(v)
    return data_by_month_per_hour