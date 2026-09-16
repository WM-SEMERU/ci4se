def _mx(domain):

    def got_records(result):
        return sorted([(int(record.payload.preference), str(record.payload.
            name)) for record in result[0]])
    d = lookupMailExchange(domain)
    d.addCallback(got_records)
    return d