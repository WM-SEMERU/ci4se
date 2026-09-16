def deactivate_version(self, service_id, version_number):
    content = self._fetch('/service/%s/version/%d/deactivate' % (service_id,
        version_number), method='PUT')
    return FastlyVersion(self, content)