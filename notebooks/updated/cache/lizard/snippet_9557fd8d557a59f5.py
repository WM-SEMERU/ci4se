def modification_time(self):
    if self._stat_info is None:
        return None
    timestamp = int(self._stat_info.st_mtime)
    return dfdatetime_posix_time.PosixTime(timestamp=timestamp)