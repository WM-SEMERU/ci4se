def end_time(self):
    try:
        try:
            return datetime.strptime(self.nc.attrs['time_coverage_end'],
                '%Y-%m-%dT%H:%M:%SZ')
        except TypeError:
            return datetime.strptime(self.nc.attrs['time_coverage_end'].
                astype(str), '%Y-%m-%dT%H:%M:%SZ')
    except ValueError:
        return datetime.strptime(self.nc.attrs['time_coverage_end'],
            '%Y%m%dT%H%M%S%fZ')