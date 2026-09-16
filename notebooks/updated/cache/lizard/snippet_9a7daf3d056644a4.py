def list_vcls(self, service_id, version_number):
    content = self._fetch('/service/%s/version/%d/vcl' % (service_id,
        version_number))
    return map(lambda x: FastlyVCL(self, x), content)