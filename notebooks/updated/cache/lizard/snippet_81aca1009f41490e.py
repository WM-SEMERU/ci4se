def timestamp(self, timezone=None):
    if timezone is None:
        timezone = self.timezone
    return self.__timestamp__ - timezone