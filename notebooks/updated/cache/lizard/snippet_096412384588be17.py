def create(cls, data=None, api_key=None, endpoint=None, add_headers=None,
    data_key=None, response_data_key=None, method='POST', **kwargs):
    inst = cls(api_key=api_key)
    if data_key is None:
        data_key = cls.sanitize_ep(cls.get_endpoint())
    if response_data_key is None:
        response_data_key = cls.sanitize_ep(cls.get_endpoint())
    body = {}
    body[data_key] = data
    if endpoint is None:
        endpoint = cls.get_endpoint()
    inst._set(cls._parse(inst.request(method, endpoint=endpoint, data=body,
        query_params=kwargs, add_headers=add_headers), key=response_data_key))
    return inst