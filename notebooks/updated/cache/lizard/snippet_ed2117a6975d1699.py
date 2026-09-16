def _legacy_request(self, method, table, **kwargs):
    warnings.warn(
        '`%s` is deprecated and will be removed in a future release. Please use `resource()` instead.'
         % inspect.stack()[1][3], DeprecationWarning)
    return LegacyRequest(method, table, request_params=self.request_params,
        raise_on_empty=self.raise_on_empty, session=self.session, instance=
        self.instance, base_url=self.base_url, **kwargs)