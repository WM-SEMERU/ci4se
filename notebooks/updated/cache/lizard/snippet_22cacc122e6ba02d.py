def _check_if_complete(self, url, json_response):
    if '__done' in json_response and isinstance(json_response, list):
        mr_parts = list(urlparse(url))
        mr_query = parse_qs(mr_parts[4])
        mr_query['mr'] = '"' + str(json_response[0]) + '"'
        mr_parts[4] = urlencode(mr_query, True)
        mr_link = urlunparse(mr_parts)
        mr_j, mr_r = self._ajax(mr_link)
        self.log.debug('MultipleRedirect link: %s', mr_link)
        return super(Installer, self)._check_if_complete(url, mr_j)
    return False