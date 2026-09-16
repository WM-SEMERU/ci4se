def CountAPIAuditEntriesByUserAndDay(self, min_timestamp=None,
    max_timestamp=None):
    results = collections.Counter()
    for entry in self.api_audit_entries:
        if min_timestamp is not None and entry.timestamp < min_timestamp:
            continue
        if max_timestamp is not None and entry.timestamp > max_timestamp:
            continue
        day = rdfvalue.RDFDatetime.FromDate(entry.timestamp.AsDatetime().date()
            )
        results[entry.username, day] += 1
    return dict(results)