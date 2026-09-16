def writegroup(self, auth, entries, defer=False):
    return self._call('writegroup', auth, [entries], defer)