def modification_time(self):
    timestamps = self._gzip_file.modification_times
    if not timestamps:
        return None
    return dfdatetime_posix_time.PosixTime(timestamp=timestamps[0])