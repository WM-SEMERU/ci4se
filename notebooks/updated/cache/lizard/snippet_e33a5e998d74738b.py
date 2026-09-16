def background_time(self):
    time = 1.0 / self.timeslide_interval
    for ifo in self.singles:
        time *= self.singles[ifo].filled_time * self.analysis_block
    return time