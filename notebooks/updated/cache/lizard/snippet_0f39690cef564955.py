def rr_history(self, query, query_type='A'):
    if query_type not in Investigate.SUPPORTED_DNS_TYPES:
        raise Investigate.UNSUPPORTED_DNS_QUERY
    if Investigate.IP_PATTERN.match(query):
        return self._ip_rr_history(query, query_type)
    return self._domain_rr_history(query, query_type)