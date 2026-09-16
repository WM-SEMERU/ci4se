def creation_time(self, timeformat='unix'):
    if self.created_at is None:
        return None
    return timeformatutils.timeformat(self.created_at, timeformat)