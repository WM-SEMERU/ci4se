def build_swagger_12_endpoints(resource_listing, api_declarations):
    yield build_swagger_12_resource_listing(resource_listing)
    for name, filepath in api_declarations.items():
        with open(filepath) as input_file:
            yield build_swagger_12_api_declaration(name, simplejson.load(
                input_file))