def lookupAllRecords(self, name, timeout=None):
    return self._lookup(name, dns.IN, dns.A, timeout)