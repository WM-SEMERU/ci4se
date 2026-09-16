def terminating_sip_domains(self):
    if self._terminating_sip_domains is None:
        self._terminating_sip_domains = TerminatingSipDomainList(self.
            _version, trunk_sid=self._solution['sid'])
    return self._terminating_sip_domains