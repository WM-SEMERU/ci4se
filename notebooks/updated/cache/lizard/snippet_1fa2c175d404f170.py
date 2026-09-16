def build(self, builder):
    builder.start('DateTimeStamp', {})
    if isinstance(self.date_time, datetime):
        builder.data(dt_to_iso8601(self.date_time))
    else:
        builder.data(self.date_time)
    builder.end('DateTimeStamp')