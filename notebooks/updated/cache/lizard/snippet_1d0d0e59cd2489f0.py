def configure_create(self, ns, definition):

    @self.add_route(ns.collection_path, Operation.Create, ns)
    @request(definition.request_schema)
    @response(definition.response_schema)
    @wraps(definition.func)
    def create(**path_data):
        request_data = load_request_data(definition.request_schema)
        response_data = definition.func(**merge_data(path_data, request_data))
        headers = encode_id_header(response_data)
        definition.header_func(headers, response_data)
        response_format = self.negotiate_response_content(definition.
            response_formats)
        return dump_response_data(definition.response_schema, response_data,
            status_code=Operation.Create.value.default_code, headers=
            headers, response_format=response_format)
    create.__doc__ = 'Create a new {}'.format(ns.subject_name)