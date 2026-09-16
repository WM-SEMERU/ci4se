def stop_tracking(self, end_time=None):
    end_time = timegm((end_time or dt.datetime.now()).timetuple())
    return self.conn.StopTracking(end_time)