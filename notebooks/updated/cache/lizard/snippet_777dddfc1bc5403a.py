def get(cls, device_server_id, custom_headers=None):
    if custom_headers is None:
        custom_headers = {}
    api_client = client.ApiClient(cls._get_api_context())
    endpoint_url = cls._ENDPOINT_URL_READ.format(device_server_id)
    response_raw = api_client.get(endpoint_url, {}, custom_headers)
    return BunqResponseDeviceServer.cast_from_bunq_response(cls._from_json(
        response_raw, cls._OBJECT_TYPE_GET))