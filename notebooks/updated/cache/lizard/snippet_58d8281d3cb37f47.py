def advice_dcv_method(cls, csr, package, altnames, dcv_method, cert_id=None):
    params = {'csr': csr, 'package': package, 'dcv_method': dcv_method}
    if cert_id:
        params['cert_id'] = cert_id
    result = cls.call('cert.get_dcv_params', params)
    if dcv_method == 'dns':
        cls.echo('You have to add these records in your domain zone :')
    cls.echo('\n'.join(result['message']))