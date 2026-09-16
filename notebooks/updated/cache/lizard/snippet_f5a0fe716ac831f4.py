def _json_to_supported(response_body):
    data = json.loads(response_body)
    supported = []
    for supported_data in data.get('supportedList', []):
        supported.append(Supported().from_json(supported_data))
    return supported