def claim(self, ttl, grace, count=None):
    if count is None:
        qs = ''
    else:
        qs = '?limit=%s' % count
    uri = '/%s%s' % (self.uri_base, qs)
    body = {'ttl': ttl, 'grace': grace}
    resp, resp_body = self.api.method_post(uri, body=body)
    if resp.status_code == 204:
        return None
    href = resp_body[0]['href']
    claim_id = href.split('claim_id=')[-1]
    return self.get(claim_id)