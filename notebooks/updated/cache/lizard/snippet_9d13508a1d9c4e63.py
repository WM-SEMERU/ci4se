def load_isd_daily_temp_data(self, start, end, read_from_cache=True,
    write_to_cache=True):
    return load_isd_daily_temp_data(self.usaf_id, start, end,
        read_from_cache=read_from_cache, write_to_cache=write_to_cache)