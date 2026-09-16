def duration(self):
    if self.time_end is None or self.time_start is None:
        return timedelta(seconds=0)
    else:
        return self.time_end - self.time_start