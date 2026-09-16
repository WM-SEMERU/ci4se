def get_certificate_issuer_configs(self, **kwargs):
    kwargs['_return_http_data_only'] = True
    if kwargs.get('asynchronous'):
        return self.get_certificate_issuer_configs_with_http_info(**kwargs)
    else:
        data = self.get_certificate_issuer_configs_with_http_info(**kwargs)
        return data