def configure_retrievefor(self, ns, definition):
    request_schema = definition.request_schema or Schema()

    @self.add_route(ns.relation_path, Operation.RetrieveFor, ns)
    @qs(request_schema)
    @response(definition.response_schema)
    @wraps(definition.func)
    def retrieve(**path_data):
        headers = dict()
        request_data = load_query_string_data(request_schema)
        response_data = require_response_data(definition.func(**merge_data(
            path_data, request_data)))
        definition.header_func(headers, response_data)
        response_format = self.negotiate_response_content(definition.
            response_formats)
        return dump_response_data(definition.response_schema, response_data,
            headers=headers, response_format=response_format)
    retrieve.__doc__ = 'Retrieve {} relative to a {}'.format(pluralize(ns.
        object_name), ns.subject_name)