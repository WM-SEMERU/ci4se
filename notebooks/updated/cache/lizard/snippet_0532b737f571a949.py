def applications(self):
    if self._applications is None:
        self._applications = ApplicationList(self._version, account_sid=
            self._solution['sid'])
    return self._applications