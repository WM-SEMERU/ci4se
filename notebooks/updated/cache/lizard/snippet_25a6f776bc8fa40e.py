def _generate_url(self, resource, query_params=None):
    resource = '{resource}?token={token}'.format(resource=resource, token=
        self.token)
    if query_params:
        resource += '&{}'.format(urlencode(query_params))
    return self.base_url_template.format(resource)