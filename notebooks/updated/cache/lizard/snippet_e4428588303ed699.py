def get_login_url(self):
    params = {'service': self.service_url}
    if self.renew:
        params.update({'renew': 'true'})
    params.update(self.extra_login_params)
    url = urllib_parse.urljoin(self.server_url, 'login')
    query = urllib_parse.urlencode(params)
    return url + '?' + query