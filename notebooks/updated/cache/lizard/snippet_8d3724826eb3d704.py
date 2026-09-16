def _to_desired_dates(self, arr):
    times = utils.times.extract_months(arr[internal_names.TIME_STR], self.
        months)
    return arr.sel(time=times)