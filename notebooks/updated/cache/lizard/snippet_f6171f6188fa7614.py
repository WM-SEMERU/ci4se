def find_time_base(self, gps, first_ms_stamp):
    t = self._gpsTimeToTime(gps.Week, gps.TimeMS)
    self.set_timebase(t - gps.T * 0.001)
    self.timestamp = self.timebase + first_ms_stamp * 0.001