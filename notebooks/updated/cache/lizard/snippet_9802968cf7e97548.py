def get_time(self):
    if self.steam_time_offset is None or self.align_time_every and time(
        ) - self._offset_last_check > self.align_time_every:
        self.steam_time_offset = get_time_offset()
        if self.steam_time_offset is not None:
            self._offset_last_check = time()
    return int(time() + (self.steam_time_offset or 0))