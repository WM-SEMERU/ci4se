def create_domain(self, service_id, version_number, name, comment=None):
    body = self._formdata({'name': name, 'comment': comment}, FastlyDomain.
        FIELDS)
    content = self._fetch('/service/%s/version/%d/domain' % (service_id,
        version_number), method='POST', body=body)
    return FastlyDomain(self, content)