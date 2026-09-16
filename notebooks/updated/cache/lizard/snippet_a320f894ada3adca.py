def add_api_key(self, name, **kwargs):
    api = self._get_api(iam.DeveloperApi)
    kwargs.update({'name': name})
    api_key = ApiKey._create_request_map(kwargs)
    body = iam.ApiKeyInfoReq(**api_key)
    return ApiKey(api.create_api_key(body))