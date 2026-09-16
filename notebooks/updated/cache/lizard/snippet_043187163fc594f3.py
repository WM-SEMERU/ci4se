def check_domains(self, service_id, version_number):
    content = self._fetch('/service/%s/version/%d/domain/check_all' % (
        service_id, version_number))
    return map(lambda x: FastlyDomainCheck(self, x), content)