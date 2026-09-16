def get_request(self):
    if self.hostname_entry:
        self.entries.append(self.hostname_entry)
    request = {}
    for entry in self.entries:
        sans = sorted(list(set(entry['addresses'])))
        request[entry['cn']] = {'sans': sans}
    if self.json_encode:
        return {'cert_requests': json.dumps(request, sort_keys=True)}
    else:
        return {'cert_requests': request}