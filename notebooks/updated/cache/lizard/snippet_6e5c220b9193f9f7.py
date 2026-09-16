def _get_api_url(self, secure=None, **formatters):
    if self.endpoint is None:
        raise NotImplementedError('endpoint must be defined on a subclass')
    if secure is None:
        secure = self.secure
    if secure:
        api_url = POSTMARK_API_URL_SECURE
    else:
        api_url = POSTMARK_API_URL
    url = urljoin(api_url, self.endpoint)
    if formatters:
        url = url.format(**formatters)
    return url