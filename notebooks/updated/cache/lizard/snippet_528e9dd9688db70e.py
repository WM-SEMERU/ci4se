def seconds_passed(self):
    return int((Date(self).datetime - self._STARTDATE.datetime).total_seconds()
        )