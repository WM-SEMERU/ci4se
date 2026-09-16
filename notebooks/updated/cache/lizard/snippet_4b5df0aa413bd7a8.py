def date(self, local=False):
    return Date(self.get(local).date(), self.local_tz)