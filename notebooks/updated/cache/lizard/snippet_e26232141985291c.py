def timestamp_pb(self):
    inst = self if self.tzinfo is not None else self.replace(tzinfo=pytz.UTC)
    delta = inst - _UTC_EPOCH
    seconds = int(delta.total_seconds())
    nanos = self._nanosecond or self.microsecond * 1000
    return timestamp_pb2.Timestamp(seconds=seconds, nanos=nanos)