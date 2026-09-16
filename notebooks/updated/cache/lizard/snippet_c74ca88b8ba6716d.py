def configure_boto_session_method_kwargs(self, service, kw):
    if service in self.endpoint_urls and not 'endpoint_url' in kw:
        kw['endpoint_url'] = self.endpoint_urls[service]
    return kw