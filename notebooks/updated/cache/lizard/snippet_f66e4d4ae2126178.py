def list_parameters(self, parameter_type=None, page_size=None):
    params = {'details': True}
    if parameter_type is not None:
        params['type'] = parameter_type
    if page_size is not None:
        params['limit'] = page_size
    return pagination.Iterator(client=self._client, path=
        '/mdb/{}/parameters'.format(self._instance), params=params,
        response_class=mdb_pb2.ListParametersResponse, items_key=
        'parameter', item_mapper=Parameter)