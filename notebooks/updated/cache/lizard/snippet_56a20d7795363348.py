def tgread_date(self):
    value = self.read_int()
    if value == 0:
        return None
    else:
        return datetime.fromtimestamp(value, tz=timezone.utc)