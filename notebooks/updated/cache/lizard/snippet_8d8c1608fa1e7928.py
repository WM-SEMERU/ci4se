def load_isd_hourly_temp_data(self, start, end, read_from_cache=True,
    write_to_cache=True, error_on_missing_years=True):
    return load_isd_hourly_temp_data(self.usaf_id, start, end,
        read_from_cache=read_from_cache, write_to_cache=write_to_cache,
        error_on_missing_years=error_on_missing_years)