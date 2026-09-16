def _post_xml(self, *args, **kwargs):
    if 'timeout' not in kwargs:
        kwargs['timeout'] = self.timeout
    req = self.session_xml.post(*args, **kwargs)
    return req