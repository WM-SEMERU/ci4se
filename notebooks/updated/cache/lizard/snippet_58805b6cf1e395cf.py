def get_domains(self):
    url = self.API_TEMPLATE + self.DOMAINS
    data = self._get_json_from_response(url)
    domains = list()
    for item in data:
        domain = item['domain']
        domains.append(domain)
        self.logger.debug('Discovered domains: {}'.format(domain))
    return domains