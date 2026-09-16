def members(self):
    if self._members is None:
        self._members = MemberList(self._version, account_sid=self.
            _solution['account_sid'], queue_sid=self._solution['sid'])
    return self._members