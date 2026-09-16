def _extract_functions(resources):
    result = {}
    for name, resource in resources.items():
        resource_type = resource.get('Type')
        resource_properties = resource.get('Properties', {})
        if resource_type == SamFunctionProvider._SERVERLESS_FUNCTION:
            layers = SamFunctionProvider._parse_layer_info(resource_properties
                .get('Layers', []), resources)
            result[name] = SamFunctionProvider._convert_sam_function_resource(
                name, resource_properties, layers)
        elif resource_type == SamFunctionProvider._LAMBDA_FUNCTION:
            layers = SamFunctionProvider._parse_layer_info(resource_properties
                .get('Layers', []), resources)
            result[name
                ] = SamFunctionProvider._convert_lambda_function_resource(name,
                resource_properties, layers)
    return result