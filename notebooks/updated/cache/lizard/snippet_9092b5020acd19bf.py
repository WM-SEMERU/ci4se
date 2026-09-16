def compliance_schedule(self, column=None, value=None, **kwargs):
    return self._resolve_call('PCS_CMPL_SCHD', column, value, **kwargs)