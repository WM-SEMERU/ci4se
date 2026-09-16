def creation_date(self):
    timestamp = self._prof.get('timecreated')
    if timestamp:
        return time.localtime(timestamp)