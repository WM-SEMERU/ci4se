def iso8601(self, tzinfo=None, end_datetime=None):
    return self.date_time(tzinfo, end_datetime=end_datetime).isoformat()