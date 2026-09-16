def _refresh_http(api_request, operation_name):
    path = 'operations/{}'.format(operation_name)
    api_response = api_request(method='GET', path=path)
    return json_format.ParseDict(api_response, operations_pb2.Operation())