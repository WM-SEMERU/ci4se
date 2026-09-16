def set_duration(self, duration):
    if self.get_duration_metadata().is_read_only():
        raise errors.NoAccess()
    if not self._is_valid_duration(duration, self.get_duration_metadata()):
        raise errors.InvalidArgument()
    map = dict()
    map['days'] = duration.days
    map['seconds'] = duration.seconds
    map['microseconds'] = duration.microseconds
    self._my_map['duration'] = map