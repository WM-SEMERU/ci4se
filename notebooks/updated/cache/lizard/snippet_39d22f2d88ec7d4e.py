def get_certificate_issuer(self, certificate_issuer_id, **kwargs):
    kwargs['_return_http_data_only'] = True
    if kwargs.get('asynchronous'):
        return self.get_certificate_issuer_with_http_info(certificate_issuer_id
            , **kwargs)
    else:
        data = self.get_certificate_issuer_with_http_info(certificate_issuer_id
            , **kwargs)
        return data