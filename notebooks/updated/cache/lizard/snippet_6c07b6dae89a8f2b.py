def _multicall_callback(self, values, calls):
    result = KojiMultiCallIterator(values)
    result.connection = self.connection
    result.calls = calls
    return result