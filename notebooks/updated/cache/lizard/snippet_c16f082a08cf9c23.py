def past(self, rev=None):
    if rev is not None:
        self.seek(rev)
    return WindowDictPastView(self._past)