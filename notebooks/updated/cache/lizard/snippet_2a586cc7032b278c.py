def prepped_value(self):
    if self._prepped is None:
        self._prepped = self._ldap_string_prep(self['value'].native)
    return self._prepped