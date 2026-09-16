def list_public_containers(self):
    resp, resp_body = self.api.cdn_request('', 'GET')
    return [cont['name'] for cont in resp_body]