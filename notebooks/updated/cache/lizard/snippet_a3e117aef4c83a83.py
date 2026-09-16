def _construct_url(self, base_api, params):
    params['key'] = self.api_key
    return super(PickPoint, self)._construct_url(base_api, params)